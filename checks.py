from collections import Counter

def check_duplicates(deals):
    """Returns issue dicts for any dealID that appears more than once"""
    ids = [deal['dealID'] for deal in deals]
    counts = Counter(ids)
    return [
        {
        "check": "duplicate_id",
        "dealID": deal_id,
        "detail": f"appears {count} times",
        }
    for deal_id, count in counts.items() if count > 1
    ]

if __name__ == "__main__":
    from fetch_deals import fetch_deals
    from clean import clean_deal

    deals = [clean_deal(d) for d in fetch_deals()]
    print("Real data:", check_duplicates(deals))

    fake = [{"dealID": "A"}, {"dealID": "A"}, {"dealID": "B"}]
    print("Fake data:", check_duplicates(fake))