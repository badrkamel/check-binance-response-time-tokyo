"""
import requests

url = "https://api.binance.com/api/v1/klines"

params = {
	'symbol': 'BTCUSDT',
	'interval': '1h'
}

response = requests.get(url, params=params)
print(response.elapsed.total_seconds())
"""

import requests

url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"

response = requests.get(url)
print(response.elapsed.total_seconds())
