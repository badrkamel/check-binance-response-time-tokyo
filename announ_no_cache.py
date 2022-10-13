import requests

url = "https://www.binance.me/bapi/composite/v1/public/cms/article/latest/query"
url2 = "https://www.binance.com/bapi/composite/v1/public/cms/article/latest/query"


for i in range(10):
    response = requests.get(f'{url}?pageSize={i}')

    print(response.elapsed.total_seconds())
    print(response.headers['X-Cache'])
