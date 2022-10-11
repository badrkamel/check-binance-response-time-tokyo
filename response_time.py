import requests

url = "https://api.binance.com/api/v1/klines"

response = requests.get(url)
print(response.elapsed.total_seconds())
