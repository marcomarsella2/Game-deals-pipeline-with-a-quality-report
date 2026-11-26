from collections import Counter

def summarise(issues):
    """Return a dictionary mapping check name -> count number of issues found"""
    return dict(Counter(issue['check'] for issue in issues))

def format_report(issues):
    """Return a human readable string report of the issues found"""
    if not issues:
        return "Data quality: PASS (0 issues found)"
    counts = summarise(issues)
    lines = [f"Data quality: FAIL ({len(issues)} issues found)"]
    for check_name, count in counts.items():
        lines.append(f"  {check_name}: {count} issue(s)")
    return "\n".join(lines)

if __name__ == "__main__":
    from fetch_deals import fetch_deals
    from clean import clean_deal
    from checks import run_all_checks

    deals = [clean_deal(d) for d in fetch_deals()]

    issues = run_all_checks(deals)
    print(format_report(issues))