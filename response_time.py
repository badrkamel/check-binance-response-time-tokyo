import requests

url = "https://api.binance.com/api/v1/klines"

params = {
	'symbol': 'BTCUSDT',
	'interval': '1h'
}

response = requests.get(url, params=params)
print(response.elapsed.total_seconds())
