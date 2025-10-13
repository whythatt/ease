import json
import time
import asyncio
import aiohttp
from typing import Union
from parser.headers import url_headers, image_headers


class AsyncParser:
    semaphore = asyncio.Semaphore(3)  # Создаем семафор один раз

    @staticmethod
    async def fetch_page(session, params, semaphore):
        async with semaphore:
            async with session.get(
                "https://ya.ru/images/api/v1/cbir/market",
                params=params,
                headers=url_headers,
            ) as response:
                response.raise_for_status()
                return await response.json()

    @staticmethod
    async def fetch_all_pages(image_url: str, page_index: int):
        params = {"url": image_url, "p": "0", "text": ""}
        goods = []
        async with aiohttp.ClientSession() as session:
            tasks = []
            for page_number in range(1, page_index + 2)[page_index - 3 : -1]:
            # for page_number in range(1, 11):
                page_params = params.copy()
                page_params["p"] = str(page_number)
                tasks.append(
                    AsyncParser.fetch_page(session, page_params, AsyncParser.semaphore)
                )

            results = await asyncio.gather(*tasks)
            for json_response in results:
                data = json_response.get("data", {}).get("images", [])
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


# parser = AsyncParser.fetch_all_pages(
#     image_url="https://i.pinimg.com/736x/56/c1/82/56c182400eb8735938bd684028b73678.jpg",
#     page_index=6,
# )

# start_time = time.perf_counter()
# data = asyncio.run(parser)
# end_time = time.perf_counter()
# print(len(data.get("products")))
# print(f"Время выполнения функции: {end_time - start_time:.4f} секунд")
# with open("parser/result.json", "w") as f:
#     json.dump(data, f, ensure_ascii=False, indent=4)
