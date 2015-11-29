# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
from scrapy.conf import settings

class MongoDBPipeline(object):

	def __init__(self):
		connection = pymongo.MongoClient(
			settings['MONGODB_SERVER'],
			settings['MONGODB_PORT']
		)

		self.db = connection[settings['MONGODB_DB']]

	def get_sites(self):
		collection_sites = self.db.sites
		return collection_sites.find()

	def create_info(self, item, url=None):
		collection_infos = self.db.infos

		data = {
			'title'        : item['title'],
			'description' : item['description'],
			'active'      : 1
		}

		collection_infos.insert(data)
