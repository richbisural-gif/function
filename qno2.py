products = [
    {'id': 1, 'name': 'laptop', 'category': 'electronics', 'price': 1200, 'instock': True},
    {'id': 2, 'name': 'smartphone', 'category': 'electronics', 'price': 800, 'instock': False}
]

# Filter products that are in stock
in_stock_products = list(filter(lambda product: product['instock'] == True, products))

# Display the result
print(in_stock_products)