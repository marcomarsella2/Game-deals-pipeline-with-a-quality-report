from collections import Counter


def check_duplicate_ids(deals):
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

def check_missing_titles(deals):
    """Flag deals whose title is empty, missing, or whitespace only."""
    return [
        {
            "check": "missing_title",
            "dealID": deal['dealID'],
            "detail": f"title is {deal.get('title')!r}",
        }
        for deal in deals
        if not deal.get('title').strip()
    ]

def check_suspicious_prices(deals):
    """Flag deals where salePrice is nonpositive or not below normalPrice"""
    issues = []
    for deal in deals:
        sale = deal.get("salePrice")
        normal = deal.get("normalPrice")
        if sale is None or normal is None:
            continue
        if sale <= 0:
            issues.append({
                "check": "suspicious_price",
                "dealID": deal['dealID'],
                "detail": f"salePrice {sale} is not positive",
            })
        elif sale >= normal:
            issues.append({
                "check": "suspicious_price",
                "dealID": deal['dealID'],
                "detail": f"salePrice {sale} >= normalPrice {normal}",
            })
    return issues

def run_all_checks(deals):
    """Run all checks and return a list of issues"""
    issues = []
    issues += check_duplicate_ids(deals)
    issues += check_missing_titles(deals)
    issues += check_suspicious_prices(deals)
    return issues

if __name__ == "__main__":
    import sys
    from fetch_deals import fetch_deals
    from clean import clean_deal

    deals = [clean_deal(d) for d in fetch_deals()]
    issues = run_all_checks(deals)
    print(f"{len(issues)} issue(s) found")
    for issue in issues:
        print(issue)
    sys.exit(1 if issues else 0)