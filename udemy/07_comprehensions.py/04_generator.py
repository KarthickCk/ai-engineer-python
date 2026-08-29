daily_sales = [5, 10, 30, 5, 3, 6, 9, 45]

total_cups = sum(sale for sale in daily_sales if sale > 5)
print(total_cups)