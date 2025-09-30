import json
import requests
from .headers import url_headers, image_headers


class Parser:
    @classmethod
    def fetch_data_by_url(self, image_url: str):
        params = {
            "url": "",
            "p": "0",
            "text": "",
        }
        params["url"] = image_url

        goods = []

        while int(params["p"]) < 2:
            # while True:
            response = requests.get(
                "https://ya.ru/images/api/v1/cbir/market",
                params=params,
                headers=url_headers,
            )

            if response.status_code != 200:
                response.raise_for_status()
            try:
                data = response.json()["data"]["images"]
            except (ValueError, AttributeError):
                return "Invalid response format"

            if not data:
                return "Goods were not found according to this link"

            for item in data:
                market_info = item.get("market_info", {})
                goods.append(
                    {
                        "image_url": market_info["Url"],
                        "title": market_info["Title"],
                        "price": market_info["Price"],
                        "shop_url": market_info["ShopUrlRaw"],
                        "shop_name": market_info["ShopName"],
                        "shop_domain": market_info["ShopDomain"],
                    }
                )

            params["p"] = str(int(params["p"]) + 1)

        return {"products": goods}

    @classmethod
    def fetch_image_url_from_file(self, binary_image: bytes):
        url = "https://ya.ru/images-apphost/image-download"
        response = requests.post(url, headers=image_headers, data=binary_image)

        if response.status_code != 200:
            response.raise_for_status()

        try:
            image_url = response.json()["url"]
            return image_url
        except (ValueError, AttributeError):
            return "Invalid response format"


# with open("socks.jpg", "rb") as f:
#     data = f.read()

# socks = Parser().fetch_data_by_image(data)
# print(socks)
