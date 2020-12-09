# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline
import scrapy
from pymongo import MongoClient
import hashlib
from scrapy.utils.python import to_bytes



class leroymerlinPipeline:

    def __init__(self):
        client = MongoClient('localhost',27017)
        self.mongo_base = client.leroymerlin

    def process_item(self, item, spider):
        collection = self.mongo_base[spider.name]
        data = {
            'name': item['name'],
            'article': item['article'][0],
            'link': item['link'][0],
            'characters_L':item['characters_L'],
            'characters_R': item['characters_R'],
            'photos':item['photos'],
            'price': item['price']
        }
        collection.insert_one(data)
        list_ch_l = item['characters_L']
        list_ch_r = item['characters_R']
        for index in range(len(list_ch_l)):
            collection = self.mongo_base[list_ch_l[index]]
            data = {
                'name':item['name'],
                'article':item['article'][0],
                'link': item['link'][0]
            }
            data['characters_L'] = list_ch_l[index]
            data['characters_R'] = list_ch_r[index]
            collection.insert_one(data)
        return item


class PhotosPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        if item['photos']:
            for img in item['photos']:
                try:
                    yield scrapy.Request(img)
                except Exception as e:
                    print(e)

    def item_completed(self, results, item, info):
        if results:
            item['photos'] = [itm[1] for itm in results if itm[0]]
        return item

    def file_path(self, request, response=None, info=None, *, item):
        away = str(item['article'][0])
        image_guid = hashlib.sha1(to_bytes(request.url)).hexdigest()
        return f'{away}/{image_guid}.jpg'



