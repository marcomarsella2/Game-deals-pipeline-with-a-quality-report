import requests

API_URL = "https://www.cheapshark.com/api/1.0/deals?storeID=1&upperPrice=15"

HEADERS = {"User-Agent": "Game-Deals/V1.0 https://github.com/marcomarsella2/Game-deals-pipeline-with-a-quality-report"}

def fetch_deals():
    response = requests.get(API_URL, headers=HEADERS)

    if response.status_code == 200:
        return response.json()
    else:
        raise RuntimeError(f"Request failed: {response.status_code}")

def print_deals(deals):
    for deal in deals[:5]:
        print(f"Title: {deal['title']} | Sale Price: ${deal['salePrice']} | Normal Price: ${deal['normalPrice']} | Savings: {round(float(deal['savings']))}%")

if __name__ == "__main__":
    deals = fetch_deals()
    print_deals(deals)