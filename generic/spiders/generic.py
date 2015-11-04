# -*- coding: utf-8 -*-
import scrapy


class GenericSpider(scrapy.Spider):
    name = "generic"
    
    allowed_domains = [
        'http://imasters.com.br',
        'http://vidadeprogramador.com.br',
        'http://winnersopensource.herokuapp.com'
    ]

    start_urls = (
        'http://imasters.com.br',
        'http://vidadeprogramador.com.br',
        'http://winnersopensource.herokuapp.com'
    )

    def parse(self, response):
        title = response.xpath("/html/head/title/text()").extract_first()
        description = response.xpath("/html/head/meta/@content").extract()
        
        print title, description