order_amount = int(input("Enter the order amount: "))

delivery_fees = 0 if order_amount > 300 else 30

print(f"The delivery fee for an order amount of ${order_amount} is ${delivery_fees}.")