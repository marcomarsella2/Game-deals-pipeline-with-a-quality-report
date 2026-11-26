from clean import clean_deal

def test_missing_metacritic_becomes_none():
    deal = {"dealID": "A", "title": "T", "storeID": "1", "salePrice": "9.99", "normalPrice": "19.99", "savings": "50"}
    assert clean_deal(deal)["metacriticScore"] is None