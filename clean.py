def clean_deal(raw):
    """Take a raw API deal and return a dictionary with proper types"""
    score = raw.get("metacriticScore")
    return {
        "dealID": raw["dealID"],
        "title": raw["title"],
        "storeID": raw["storeID"],
        "gameID": raw.get("gameID"),
        "salePrice": float(raw["salePrice"]),
        "normalPrice": float(raw["normalPrice"]),
        "savings": float(raw["savings"]),
        "metacriticScore": int(score) if score else None,

    }