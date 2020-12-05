# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst

def change_photo_url(url):
    if url:
        url = url.replace(',w_82',',w_1200')
        url = url.replace(',h_82', ',h_1200')
    return url

def change_price(price):
    price = price.replace(' ','')
    try:
        float(price)
        return float(price)
    except ValueError:
        return price


def change_character_r(price):
    price = price.replace('  ','')
    price = price.replace('\n', '')

    if price == 'Да':
        return True
    elif price == 'Нет':
        return False

    elif price.isdigit():
        return float(price)
    else:
        try:
            float(price)
            return float(price)
        except ValueError:
            return price
    return price #На всякий случай


class leroymerlinItem(scrapy.Item):

    name = scrapy.Field(output_processor = TakeFirst())
    photos = scrapy.Field(input_processor = MapCompose(change_photo_url))
    characters_L = scrapy.Field(input_processor=MapCompose())
    characters_R = scrapy.Field(input_processor=MapCompose(change_character_r))
    price = scrapy.Field(input_processor=MapCompose(change_price))
    link = scrapy.Field(input_processor=MapCompose())
    article = scrapy.Field(input_processor=MapCompose())
    _id = scrapy.Field()

