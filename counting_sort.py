from products_list import products

def calculate_total(products):
    total_price = sum(product['price'] for product in products)
    product_count = len(products)
    return product_count, total_price


product_count, total_price = calculate_total(products)


print(f"Total number of products: {product_count}")
print(f"Total price of all products: ${total_price:.2f}")