#Файл паука - парсит данные со страниц
import scrapy
from scrapy.http import HtmlResponse
from jobparser.items import JobparserItem

class HhruSpider(scrapy.Spider):
    name = 'hhru'
    allowed_domains = ['hh.ru']   # Список разрешенных доменов
    start_urls = ['https://hh.ru/search/vacancy?area=&fromSearchLine=true&st=searchVacancy&text=python']

    # Метод parse является точкой входа. Он принимает response от get-запроса по ссылке в start_urls
    def parse(self, response: HtmlResponse):
        # Получаем список ссылок на вакансии на странице

        vacancies_links = response.xpath("//span/a[contains(@class,'bloko-link')]/@href").extract()
        for link in vacancies_links:  # Перебираем полученные ссылки
            yield response.follow(link, callback=self.vacansy_parse)

        # Ищем ссылку на след. страницу с вакансиями
        next_page = response.xpath("//a[contains(@class,'HH-Pager-Controls-Next')]/@href").extract_first()
        if next_page:
            yield response.follow(next_page, callback=self.parse) # Рекурсия для повторной обработки страницы
        else:
            return  # Если ссылки на следю страницу не существует

    # Метод для обработки страницы с вакансией
    def vacansy_parse(self, response:HtmlResponse):
        name = response.xpath("//h1/text()").extract_first()
        salary = response.xpath("//p[@class='vacancy-salary']//text()").extract()
        link = response.url
        sites= 'hh.ru'
        yield JobparserItem(item_name=name, item_salary=salary,item_link=link,item_sites=sites)  # Передаем собранные данные в структуру items

