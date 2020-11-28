# Для запуска нашего паука. Удобно для отладки
# Подключаем основные классы scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

# Подключаем наши файлы (классы пауков и настройки)
from jobparser.spiders.hhru import HhruSpider
from jobparser.spiders.sjru import SjruSpider
from jobparser import settings

if __name__ == '__main__':
    # создаем объект с настройками
    crawler_settings = Settings()
    crawler_settings.setmodule(settings)

    # создаем объект процесса для работы паука
    process = CrawlerProcess(settings=crawler_settings)
    process.crawl(HhruSpider)
    process.crawl(SjruSpider)

    process.start()   # Запускаем паука
