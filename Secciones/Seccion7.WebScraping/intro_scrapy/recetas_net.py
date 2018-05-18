# -*- coding: utf-8 -*-
import scrapy


class RecetasNetSpider(scrapy.Spider):
    name = 'recetas_net'
    allowed_domains = ['recetas.net']
    start_urls = [
            'http://www.recetas.net/tipo-plato-busqueda/14/Pastas-y-arroces',
            "http://www.recetas.net/tipo-plato-busqueda/12/Sopas-y-cremas",
            "http://www.recetas.net/tipo-plato-busqueda/15/Entradas-y-huevos",
            "http://www.recetas.net/tipo-plato-busqueda/9/Ensaladas-y-verduras",
            ]

    def parse(self, response):
        urls_recetas = list(
                        map(
                            response.urljoin,
                            response.css("a.whiteBtn::attr(href)").extract()
                            )
                        )
        for url_receta in urls_recetas:
            yield scrapy.Request(url_receta, callback=self.procesar_receta)           
          
        siguiente_pagina_url = response.urljoin(response.css("a.next::attr(href)").extract_first())
        if siguiente_pagina_url:
            yield scrapy.Request(siguiente_pagina_url)
            
    def procesar_receta(self, response):
        
        categoria = response.css("h2 a::text").extract_first() 
        titulo = response.css("section.receta h1::text").extract_first().strip().capitalize() 
        
        instrucciones = response.css("div.elaboracion p::text").extract()
        instrucciones = list(map(lambda x: x.strip("\r\n "),instrucciones))
        instrucciones = ''.join(instrucciones)
       
        ingredientes = response.css("div.ingredientes li::text").extract()
    
        puntuacion = response.css("div.otrosDet div.score span::text").extract_first().strip()
        
        detalles = response.css("div.otrosDet p strong::text").extract() 
        detalles = list(map(lambda d: d.replace("\r\n                ",""), detalles))
    
        yield {
            "categoria": categoria,
            "ingredientes": ingredientes,
            "instrucciones": instrucciones,
           "titulo": titulo,
           "puntuacion": puntuacion, 
           "dificultad": detalles[0],
           "tiempo": detalles[2],
           "vegetariana": detalles[3],
           "calorias": detalles[4]
            }