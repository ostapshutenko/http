# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient

# Класс пайплайна для обработки собранных данных
class JobparserPipeline:

    def __init__(self):   # Конструктор для осуществления подключения к монго
        client = MongoClient('localhost', 27017)
        self.mongo_base = client['scrapy']  # Имя базы

    def process_item(self, item, spider):    # Точка входа для обработки item'a

        if spider.name == 'hhru':
            collection = self.mongo_base[spider.name]  # Выбираем коллекцию по имени паука
            collection.insert_many(item)
        elif spider.name == 'sjru':
            collection = self.mongo_base[spider.name]  # Выбираем коллекцию по имени паука
            collection.insert_many(item)
        return item



    # def salary(self, salary):
    #     pass
    #
    #     return min_salary, max_salary, cur