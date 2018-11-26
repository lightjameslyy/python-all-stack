# 1. input price of apple
price_str = input("price of apple per Kg: ")
price = float(price_str)


# 2. input weight of apples
weight_str = input("weight of apples: ")
weight = float(weight_str)

# 3. calculate money
money = weight * price

print(money)