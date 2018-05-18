# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest


class QuotesSpider(scrapy.Spider):
    name = 'frases_splash'
    start_urls = ['http://quotes.toscrape.com/js']

    def start_requests(self):
        yield SplashRequest(url=self.start_urls[0], callback=self.parse)

    def parse(self, response):
        frases = response.css("div.quote")
        for frase in frases:
            yield self.procesar_frase(frase)
        siguiente_pagina = response.urljoin(response.css("li.next>a::attr(href)").extract_first())
        if siguiente_pagina:
            yield SplashRequest(siguiente_pagina)

    def procesar_frase(self, frase):
        texto_frase = frase.css("span.text::text").extract_first()
        autor = frase.css("small.author::text").extract_first()
        etiquetas = frase.css("div.tags>a::text").extract()
        return {
            "autor": autor,
            "frase": texto_frase,
            "etiquetas": etiquetas
        }
