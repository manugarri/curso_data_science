# -*- coding: utf-8 -*-
import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/js/']

    def parse(self, response):
        for frase in response.css("div.quote"):
            yield self.procesar_frase(frase)
        
        siguiente_pagina = response.urljoin(response.css("li.next>a::attr(href)").extract_first())
        if siguiente_pagina:
            yield scrapy.Request(siguiente_pagina)

    def procesar_frase(self, frase):
        texto_frase = frase.css("span.text::text").extract_first()
        autor = frase.css("small.author::text").extract_first()
        etiquetas = frase.css("div.tags>a::text").extract()
        return {
            "autor": autor,
            "frase": texto_frase,
            "etiquetas": etiquetas
        }