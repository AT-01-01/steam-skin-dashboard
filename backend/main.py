from fastapi import FastAPI
import httpx

app = FastAPI()

STEAM_INVENTORY_URL = "https://steamcommunity.com/inventory/{steamid}/730/2?l=english&count=5000"
BUFF_SEARCH_URL = "https://buff.163.com/api/market/goods/sell_order"
STEAM_PRICE_URL = "https://steamcommunity.com/market/priceoverview/"

client = httpx.AsyncClient(headers={
    "User-Agent": "Mozilla/5.0"
})

# 1. 获取 Steam 库存
@app.get("/inventory/{steamid}")
async def get_inventory(steamid: str):
    url = STEAM_INVENTORY_URL.format(steamid=steamid)
    r = await client.get(url)
    return r.json()

# 2. Buff 实时最低价
@app.get("/buff_price")
async def buff_price(name: str, goods_id: int):
    params = {
        "goods_id": goods_id,
        "page_num": 1,
        "sort_by": "price.asc"
    }
    r = await client.get(BUFF_SEARCH_URL, params=params)
    data = r.json()
    try:
        price = data["data"]["items"][0]["price"]
    except:
        price = None
    return {"buff_lowest": price}

# 3. Steam 实时最低价
@app.get("/steam_price")
async def steam_price(name: str):
    params = {
        "country": "CN",
        "currency": 23,
        "appid": 730,
        "market_hash_name": name
    }
    r = await client.get(STEAM_PRICE_URL, params=params)
    return r.json()
