def price_category(price):
    if price < 50:
        return "Budget"
    elif 50 <= price <= 100:
        return "Mid-range"
    else:
        return "Premium"