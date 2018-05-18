# -*- coding: utf-8 -*-
import scrapy


class PostsSpider(scrapy.Spider):
    name = 'posts'
    allowed_domains = ['meneame.net']
    start_urls = ['http://meneame.net/']

    def parse(self, response):
        #obtenemos las noticias principales
        noticias = response.css("div.news-summary")
        
        #por cada noticia producimos el output de dicha noticia
        for noticia in noticias:
            yield self.procesar_noticia(noticia)
        
        #encontramos la pagina siguiente
        pagina_siguiente = response.urljoin(response.css("div.pages a::attr(href)").extract()[-1])
        yield scrapy.Request(pagina_siguiente)
            

    def procesar_noticia(self, noticia):
        datos_noticia = {}
        datos_noticia["url"] = noticia.css("h2>a::attr(href)").extract_first()
        datos_noticia["titular"] = noticia.css("h2>a::text").extract_first().strip()
        datos_noticia["n_comentarios"] = noticia.css("a.comments::text").extract()[1].strip()
        datos_noticia["karma"] = noticia.css("span.karma-value::text").extract_first().strip()
        datos_noticia["descripcion"] = noticia.css("div.news-content::text").extract_first()
        datos_noticia["n_meneos"] = noticia.css("div.votes>a::text").extract_first()
        datos_noticia["n_clics"] = noticia.css("div.clics::text").extract_first().strip()
        datos_noticia["votos_positivos"] = noticia.css("span.votes-up>span>strong::text").extract_first()
        datos_noticia["votos_negativos"] = noticia.css("span.votes-down>span>strong::text").extract_first()
        datos_noticia["votos_anonimos"] = noticia.css("span.votes-anonymous>span>strong::text").extract_first()
        datos_noticia["sub"] = noticia.css("a.subname::text").extract_first()
        datos_noticia["usuario"] = noticia.css("div.news-submitted>a::text").extract_first()
        datos_noticia["timestamp"] = noticia.css("span.ts::attr(data-ts)").extract_first()
        return datos_noticia
        