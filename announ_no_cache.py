import aiohttp
from time import sleep
from fake_headers import Headers
from asyncio import get_event_loop


url = "https://www.binance.me/bapi/composite/v1/public/cms/article/latest/query"
url2 = "https://www.binance.com/bapi/composite/v1/public/cms/article/latest/query"

header = Headers(
    headers=True
)

async def run_app():
    for i in range(1000):

        async with aiohttp.ClientSession() as session:
            async with session.get(f'{url}?pageSize={i}', headers=header.generate()) as response:

                # print(response.)
                # print(response.headers)
                print(response.headers['X-Cache'])
                sleep(.2)


get_event_loop().run_until_complete(run_app())
