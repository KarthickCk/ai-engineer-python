tea_prices = {
    "masala": 40,
    "ginger": 20,
    "green": 60
}

tea_prices_usd = {tea:price/80 for tea, price in tea_prices.items()}
print(tea_prices_usd)