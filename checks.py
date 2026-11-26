from collections import Counter

def check_duplicates_ids(deals):
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

def run_all_checks(deals):
    """Run all checks and return a list of issues"""
    issues = []
    issues += check_duplicates_ids(deals)
    return issues

if __name__ == "__main__":
    from fetch_deals import fetch_deals
    from clean import clean_deal

    deals = [clean_deal(d) for d in fetch_deals()]
    issues = run_all_checks(deals)
    print(f"{len(issues)} issue(s) found")
    for issue in issues:
        print(issue)