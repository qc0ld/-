import json
import os
import requests
import time

for fl in os.listdir('C:/Users/Илья/Documents/docs/pagination'):

    f = open('C:/Users/Илья/Documents/docs/pagination/{}'.format(fl), encoding='utf8')
    jsonText = f.read()
    f.close()

    jsonObj = json.loads(jsonText)

    for v in jsonObj['items']:
        req = requests.get(v['url'])
        data = req.content.decode()
        req.close()

        fileName = 'C:/Users/Илья/Documents/docs/vacancies/{}.json'.format(v['id'])
        f = open(fileName, mode='w', encoding='utf8')
        f.write(data)
        f.close()

        time.sleep(0.25)

print('Вакансии собраны')