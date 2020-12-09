from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

from leroymerlin import settings
from leroymerlin.spiders.leroymerlin import leroymerlinSpider


if __name__ =='__main__':


    crawler_settings = Settings()
    crawler_settings.setmodule(settings)

    process = CrawlerProcess(settings = crawler_settings)
    process.crawl(leroymerlinSpider, search = 'ковер')

    process.start()





