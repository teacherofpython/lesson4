
prices = {"алма": 200, "банан": 150, "өрік": 300, "шие": 400}
cart = []
for fruit, price in prices.items():
    if price >250:
        cart.append(fruit)
print(cart)
