from pprint import pprint
from lxml import html
import requests
from datetime import datetime
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.77 YaBrowser/20.11.0.817 Yowser/2.5 Safari/537.36'}


header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.77 YaBrowser/20.11.0.817 Yowser/2.5 Safari/537.36'}

link = 'https://lenta.ru/'

response = requests.get(link,headers=header)

#pprint(response.text)
root = html.fromstring(response.text)
#pprint(response.text)
news_head = root.xpath("//section[contains(@class,'row b-top7-for-main js-top-seven')]/div/div")
#pprint(news_head)
dat={
    'name':[],
    'link':[],
    'date':[],
    'sites-resources':[]
}

for i in range(1,7):
    dat['name'].append(news_head[i].xpath(".//a/text()")[0])
    dat['link'].append(link + news_head[i].xpath(".//a//@href")[0])
    dat['date'].append(news_head[i].xpath(".//*/time/@datetime")[0])
    dat['sites-resources'].append('lenta.ru')
#pprint(dat)

link = 'https://news.mail.ru/'



response = requests.get(link, headers=header)

#pprint(response.text)
root = html.fromstring(response.text)
#pprint(response.text)
news_head = root.xpath("//body/div[9]/div[2]/div[1]/div[1]/div[2]/ul[1]/li")

def link_and_res(link):
    #незнаю в чем проблема но не хочет подключаться к сайту пишет, что не правильный формат ссылки когда  я сюда передаю ссылку  slink (в цикле при обработки mail.ru), но работает если я скопирую эту ссылку вручную

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.77 YaBrowser/20.11.0.817 Yowser/2.5 Safari/537.36'}

    syte = requests.get(link[0],headers=headers)
    roots = html.fromstring(syte.text)
    return(roots.xpath("//a[contains(@class,'link color_gray breadcrumbs__link')]//text()"),roots.xpath("//span[contains(@class,'note__text breadcrumbs__text js-ago')]/@datetime"))


#pprint(news_head)
for item in news_head:
    slink = item.xpath(".//a/@href")
#    pprint(slink)

    dat['name'].append(item.xpath(".//text()")[0])
    dat['link'].append(slink[0])
    # ПОСМОТРИТЕ КОММЕНТРАИЙ В ФУНЦИИ  link_and_res
    (a,b) = link_and_res(slink)
    dat['sites-resources'].append(a[0])
    dat['date'].append(b[0])
#pprint(dat)


link = 'https://yandex.ru/news/'



response = requests.get(link, headers=header)

#pprint(response.text)
root = html.fromstring(response.text)
#pprint(response.text)
news_head = root.xpath("//div[contains(@class,'mg-grid__row mg-grid__row_gap_8 news-top-stories news-app__top')]/div")

#pprint(news_head)

"""
def link_add(link):
    response3 = requests.get(str(link[0]), headers=header)
    root3 = html.fromstring(response3.text)
    s = root3.xpath("//a[contains(@class,'news-story__subtitle')]//text()")
    print(s)
    return root3.xpath("//body/div[@id='neo-page']/div[1]/div[2]/div[1]/div[1]/article[1]/div[1]/a[1]/@href")
"""

for item in news_head:
    dat['link'].append(item.xpath(".//a[contains(@class,'news-card__link')]/@href")[0])
    dat['name'].append(item.xpath(".//a[contains(@class,'news-card__link')]//text()")[0])
    dat['date'].append(str(datetime.now().date()) +' '+ item.xpath(".//span[@class='mg-card-source__time']//text()")[0])
    dat['sites-resources'].append(item.xpath(".//span[@class='mg-card-source__source']//text() ")[0])
pprint(dat)

data = list()

for d in range(len(dat['name'])):
    data.append(
        {
            'link': dat['link'][d],
            'name':dat['name'][d],
            'date':dat['date'][d],
            'sites-resources':dat['sites-resources'][d]
        }
    )

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client['test_database']

db.news.insert_many(data)