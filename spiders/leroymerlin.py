import scrapy
from scrapy.http import HtmlResponse
from leroymerlin.items import leroymerlinItem
from scrapy.loader import ItemLoader

class leroymerlinSpider(scrapy.Spider):
    name = 'leroymerlin'
    allowed_domains = ['leroymerlin.ru']

    def __init__(self, search):
        super(leroymerlinSpider, self).__init__()
        self.start_urls = [f'https://leroymerlin.ru/search/?q={search}']

    def parse(self, response:HtmlResponse):

        goods_links = response.xpath("//a[@class='plp-item__info__title']/@href").extract()

        for link in goods_links:
            yield response.follow(('https://leroymerlin.ru'+link), callback=self.parse_good)

        next_page = response.xpath("//a[@rel = 'next'][1]/@href").extract_first()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
        else:
            return

    def parse_good(self, response:HtmlResponse):
        loader = ItemLoader(item=leroymerlinItem(), response=response)
        loader.add_xpath('name',"//h1/text()")
        loader.add_xpath('photos',"//uc-pdp-media-carousel/img/@src")
        loader.add_xpath('characters_L',"//dl[@class='def-list']/div/dt/text()")
        loader.add_xpath('characters_R', "//dl[@class='def-list']/div/dd/text()")
        loader.add_xpath('price', "//uc-pdp-price-view/span//text()")
        loader.add_xpath('article', "//span[@slot='article']/@content")
        loader.add_value('link',response.url)
        yield loader.load_item()



