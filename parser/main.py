import base64
import json
import requests


headers = {
    "accept": "*/*",
    "accept-language": "en-GB,en;q=0.9",
    "content-type": "application/json",
    "priority": "u=1, i",
    "referer": "https://ya.ru/images/search?rpt=imageview&url={0}&cbir_id=1607854%2FRHa06BbX0xLdOXG84NcABw9773&cbir_id=1607854%2FRHa06BbX0xLdOXG84NcABw9773&cbird=188&cbir_page=products",
    "sec-ch-ua": '"Not;A=Brand";v="99", "Brave";v="139", "Chromium";v="139"',
    "sec-ch-ua-arch": '"arm"',
    "sec-ch-ua-bitness": '"64"',
    "sec-ch-ua-full-version-list": '"Not;A=Brand";v="99.0.0.0", "Brave";v="139.0.0.0", "Chromium";v="139.0.0.0"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": '""',
    "sec-ch-ua-platform": '"macOS"',
    "sec-ch-ua-platform-version": '"13.5.0"',
    "sec-ch-ua-wow64": "?0",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "sec-gpc": "1",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
}

params = {
    "url": "",
    "p": "0",
    "text": "",
}


def fetch_data(image_url, headers=headers, params=params):
    params = params.copy()
    params["url"] = image_url

    goods = []
    while int(params["p"]) <= 1:
        response = requests.get(
            "https://ya.ru/images/api/v1/cbir/market",
            params=params,
            headers=headers,
        )

        if response.status_code == 200:
            data = response.json()["data"]["images"]
            if data:
                for d in data:
                    d = d["market_info"]
                    goods.append(
                        {
                            "image_url": d["Url"],
                            "title": d["Title"],
                            "price": d["Price"],
                            "shop_url": d["ShopUrlRaw"],
                            "shop_name": d["ShopName"],
                            "shop_domain": d["ShopDomain"],
                        }
                    )
            else:
                break
        else:
            return response.raise_for_status()

        params["p"] = str(int(params["p"]) + 1)

    return {"products": goods}

# print(fetch_data('https://i.pinimg.com/736x/d9/8f/e7/d98fe7268505fc15bca1ffe1284f883b.jpg'))
