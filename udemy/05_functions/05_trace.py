def add_vat(price, vat_rate):
    return price * (100 + vat_rate) / 100

orders = [100, 200, 300]
for order in orders:
    total_price = add_vat(order, 10)
    print(f"Total price including VAT for order {order} is: {total_price}")

