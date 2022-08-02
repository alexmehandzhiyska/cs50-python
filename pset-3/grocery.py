products = {}

while True:
    try:
        product = input().upper()

        if product in products.keys():
            products[product] += 1
        else:
            products[product] = 1
    except:
        break

sorted_products = sorted(products.items())

for product, quantity in sorted_products:
    print(f'{quantity} {product}')