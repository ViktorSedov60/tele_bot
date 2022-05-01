import requests
import json
from API_key import API_TOKEN

data = {'custname': 'viktor',
'custtel': '+72356523212',
'custemail': 'rere@mail.ru',
'size': 'large',
'topping': 'mushroom',
'comments': '',
}

params = {'q' : 'Анапа', 'appid' : API_TOKEN, 'units' : 'metric'}

headers = {

    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.141 YaBrowser/22.3.3.852 Yowser/2.5 Safari/537.36",

  }

# with open('/var/cache/cbr/daily_json.js') as data_file:
#     data = json.load(data_file)
#
# print(data['Valute']['USD']['Value'])
variable = requests.Session()
aaa = variable.get('https://httpbin.org/form/post')
responce = variable.post('https://httpbin.org/post', headers=headers, data=data, allow_redirects=True)



# responce = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
# x = responce.json()
# x['weather'][0]['main']
# # if responce:

print(responce.status_code)
# print(responce.headers)
# print(responce.content)
# aa =json.loads(responce.content)
# aa = responce.json()
# print(aa)

# aaa = (aa['rates'])
# # aaa = (aa['Valute'])
# # print(aaa)
# print(aa['date'])
# print(aaa['USD'])
# print(aaa['EUR'])
print(responce.text)



# print(responce.headers)
# print(responce.text)
# aaa = aa['0']
# print(aaa)