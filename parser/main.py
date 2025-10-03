import json
import asyncio
import aiohttp
from typing import Union
from parser.headers import url_headers, image_headers


class AsyncParser:
    @classmethod
    async def fetch_data_by_url(cls, image_url: str) -> Union[dict, str]:
        params = {
            "url": image_url,
            "p": "0",
            "text": "",
        }

        goods = []

        async with aiohttp.ClientSession() as session:
            while int(params["p"]) < 10:
            # while True:
                async with session.get(
                    "https://ya.ru/images/api/v1/cbir/market",
                    params=params,
                    headers=url_headers,
                ) as response:
                    if response.status != 200:
                        response.raise_for_status()
                    try:
                        json_response = await response.json()
                        data = json_response.get("data", {}).get("images", [])
                    except Exception:
                        return "Invalid response format"

                    if not data:
                        return "Goods were not found according to this link"

                    for item in data:
                        market_info = item.get("market_info", {})
                        goods.append(
                            {
                                "image_url": market_info.get("Url"),
                                "title": market_info.get("Title"),
                                "price": market_info.get("Price"),
                                "shop_url": market_info.get("ShopUrlRaw"),
                                "shop_name": market_info.get("ShopName"),
                                "shop_domain": market_info.get("ShopDomain"),
                            }
                        )
                    params["p"] = str(int(params["p"]) + 1)

        return {"products": goods}

    @classmethod
    async def fetch_image_url_from_file(cls, binary_image: bytes) -> Union[str, None]:
        url = "https://ya.ru/images-apphost/image-download"
        async with aiohttp.ClientSession() as session:
            async with session.post(
                url, headers=image_headers, data=binary_image
            ) as response:
                if response.status != 200:
                    response.raise_for_status()
                try:
                    json_response = await response.json()
                    image_url = json_response.get("url")
                    return image_url
                except Exception:
                    return "Invalid response format"


# parser = AsyncParser.fetch_data_by_url(
#     "https://i.pinimg.com/1200x/57/a7/a2/57a7a2cf8a43484fec7e034c684e474a.jpg"
# )
# data = asyncio.run(parser)
# print(len(data.get('products')))
# with open('parser/result.json', 'w') as f:
#     json.dump(data, f, ensure_ascii=False, indent=4)
