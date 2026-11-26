from checks import check_duplicate_ids, check_missing_titles

def test_duplicate_ids_fires_on_duplicate():
    deals = [{"dealID": "A"}, {"dealID": "A"}, {"dealID": "B"}]
    issues = check_duplicate_ids(deals)
    assert len(issues) == 1
    assert issues[0]["dealID"] == "A"
    assert issues[0]["check"] == "duplicate_id"

def test_duplicate_ids_no_issues_on_unique():
    deals = [{"dealID": "A"}, {"dealID": "B"}]
    assert check_duplicate_ids(deals) == []

def test_missing_titles_handles_none():
    deals = [{"dealID": "A", "title": None}]
    issues = check_missing_titles(deals)
    assert len(issues) == 1
    