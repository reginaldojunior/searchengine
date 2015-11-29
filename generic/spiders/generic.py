# -*- coding: utf-8 -*-
import scrapy
from ..items import GenericItem
from ..pipelines import MongoDBPipeline

class GenericSpider(scrapy.Spider):
    name = "generic"
    
    MongoDB = MongoDBPipeline()
    
    sites_list  = []
    for site in MongoDB.get_sites():
        sites_list.append(site['url'])

    allowed_domains = sites_list
    start_urls = tuple(sites_list)

    def parse(self, response):
        title = response.xpath("/html/head/title/text()").extract_first()
        description = response.xpath("/html/head/meta/@content").extract()
        
        item = GenericItem()
        item['title'] = title
        item['description'] = description
        item['url'] = response.url

        self.MongoDB.create_info(item)