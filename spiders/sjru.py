import scrapy
from scrapy.http import HtmlResponse
from jobparser.items import JobparserItem

class SuperJobSpider(scrapy.Spider):
    name = 'sjru'
    allowed_domains = ['superjob.ru']
    start_urls = ['https://www.superjob.ru/vacancy/search/']

    # Метод parse является точкой входа. Он принимает response от get-запроса по ссылке в start_urls
    def parse(self, response: HtmlResponse):
        # Получаем список ссылок на вакансии на странице
        vacancies_links = response.xpath("//a[contains(@class,'_6AfZ9')]/@href").extract()
        for link in vacancies_links:  # Перебираем полученные ссылки
            yield response.follow(link, callback=self.vacansy_parse)

        # Ищем ссылку на след. страницу с вакансиями
        next_page = response.xpath("//a[contains(@rel,'next')]/@href").extract_first()
        if next_page:
            yield response.follow(next_page, callback=self.parse)  # Рекурсия для повторной обработки страницы
        else:
            return  # Если ссылки на следю страницу не существует

    # Метод для обработки страницы с вакансией
    def vacansy_parse(self, response: HtmlResponse):
        name = response.xpath("//h1/text()").extract_first()
        salary = response.xpath("//span[contains(@class,'ZON4b')]//text()").extract()
        link = response.url
        vacancy_source = self.allowed_domains[0]
        yield JobparserItem(item_name=name, item_salary=salary, item_link=link, item_source=vacancy_source)