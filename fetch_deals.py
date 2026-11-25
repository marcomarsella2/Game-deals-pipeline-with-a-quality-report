import requests

API_URL = "https://www.cheapshark.com/api/1.0/deals?storeID=1&upperPrice=15"

HEADERS = {"User-Agent": "Game-Deals/V1.0 https://github.com/marcomarsella2/Game-deals-pipeline-with-a-quality-report"}
response = requests.get(API_URL, headers=HEADERS)

if response.status_code == 200:
    deals = response.json()
    print(deals[0])
else:
    print("Request failed:", response.status_code)
    print(response.text[:300])


for deal in deals[:5]:
    print(f"Title: {deal['title']} | Sale Price: ${deal['salePrice']} | Normal Price: ${deal['normalPrice']} | Savings: {round(float(deal['savings']))}%")