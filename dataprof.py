from pprint import pprint
import json
from bs4 import BeautifulSoup as bs
import requests
link = 'https://taganrog.hh.ru/search/vacancy'

#clusters=true&enable_snippets=true&no_magic=true&text=ассистент+HR&showClusters=false


params = {

    'text':'ассистент HR',

    'page':0
}
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.77 YaBrowser/20.11.0.817 Yowser/2.5 Safari/537.36'}
data ={
    'name_vacansy':[],
    'pay':[],
    'link':[],
    'sites':[]

}
first_step = list()
while(True):
    response = requests.get((link), params=params, headers=headers)
    if response.ok:
        soup = bs(response.text, 'html.parser')
        first_step = soup.find_all('div',{'class':'vacancy-serp-item'})
        for serial in first_step:
            s = serial.find('a', {'class': 'bloko-link HH-LinkModifier'})
            data['name_vacansy'].append(s.text)
            data['link'].append(str(s['href']))
            min_pay = str( 0)
            max_pay = str(0)
            val=''

            cstr = str(serial.find('div', {'class': 'vacancy-serp-item__sidebar'}).getText())
            #cstr = cstr.replace(u'\xa0', '')
            if len(cstr)>3:
                if cstr.find('бел.') > -1:
                    val = 'бел. руб.'
                    cstr = cstr[0:len(cstr)-9]
                else:
                    val = cstr[len(cstr) - 4:len(cstr):1]
                    cstr = cstr[0:len(cstr)-4]

                if cstr.find('до') > -1:
                    cstr = cstr.replace('до', '')
                    max_pay=cstr
                elif cstr.find('от') > -1:
                    cstr = cstr.replace('от', '')
                    min_pay = cstr
                    max_pay = ''
                elif cstr.find('-')>0:
                    (min_pay, max_pay) = cstr.split('-')


            data['pay'].append((min_pay,max_pay,val))
            data['sites'].append( link)

        params['page'] += 1

    else:
        break;
pprint(data)




link = 'https://www.superjob.ru/vacancy/search/'

# clusters=true&enable_snippets=true&no_magic=true&text=ассистент+HR&showClusters=false


params = {

    'keywords': 'ассистент HR',
    'noGeo':'1',
    'page': 0
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.77 YaBrowser/20.11.0.817 Yowser/2.5 Safari/537.36'}

#data = {'name_vacansy': [], 'pay': [], 'link': [], 'sites': []}
first_step = list()
while (True):
    response = requests.get((link), params=params, headers=headers)
    if response.ok:
        soup = bs(response.text, 'html.parser')
        first_step = soup.find_all('div', {'class': 'jNMYr GPKTZ _1tH7S'})
        #print(first_step)
        for serial in first_step:
            s = serial.find('a')
            #print(s)
            data['name_vacansy'].append(s.text)
            data['link'].append(str(s['href']))
            min_pay = str(0)
            max_pay = str(0)
            val = ''

            cstr = str(serial.find('span', {'class': '_1OuF_ _1qw9T f-test-text-company-item-salary'}).getText())
            #print (cstr)
            cstr = cstr.replace(u'\xa0', '')
            if len(cstr) > 3:
                if cstr.find('По договорённости')>-1:
                    val = 'По договорённости'
                else:

                    val = cstr[len(cstr) - 10:len(cstr):1]
                    cstr = cstr[0:len(cstr) - 10]

                    if cstr.find('до') > -1:
                        cstr = cstr.replace('до', '')
                        max_pay = cstr
                    elif cstr.find('от') > -1:
                        cstr = cstr.replace('от', '')
                        min_pay = cstr
                        max_pay = ''
                    elif cstr.find('-') > 0:
                        (min_pay, max_pay) = cstr.split('-')

            data['pay'].append((min_pay, max_pay, val))
            data['sites'].append(link)

        params['page'] += 1

    else:
        break;
pprint(data)