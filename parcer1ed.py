import requests
import json
import time
import os


def getPage(page=0):
    params = {
        'text': 'NAME:программист',
        'area': 1,  
        'page': page,
        'per_page': 100
    }

    req = requests.get('https://api.hh.ru/vacancies', params)
    data = req.content.decode()
    req.close()
    return data


for page in range(0, 20):


    jsObj = json.loads(getPage(page))


    nextFileName = 'C:/Users/Илья/Documents/docs/pagination/{}.json'.format(len(os.listdir('C:/Users/Илья/Documents/docs/pagination')))

    f = open(nextFileName, mode='w', encoding='utf8')
    f.write(json.dumps(jsObj, ensure_ascii=False))
    f.close()

    if (jsObj['pages'] - page) <= 1:
        break

    time.sleep(0.25)

print('Старницы поиска собраны')