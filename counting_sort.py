from products_list import products

""" 1. Function to count total products and calculate the total price """
def calculate_total(products):
    total_price = sum(product['price'] for product in products)
    product_count = len(products)
    return product_count, total_price


product_count, total_price = calculate_total(products)


# print(f"Total number of products: {product_count}")
# print(f"Total price of all products: ${total_price:.2f}")

""" 2. Count Products with Same Price """
def same_price_count(products):
    price_count = {}
    for product in products:
        price = product['price']
        if price in price_count:
            price_count[price] += 1
        else:
            price_count[price] = 1
    return price_count


price_count = same_price_count(products)

# print("Products count by price:")
# for price, count in price_count.items():
#     print(f"${price:.2f}: {count} product")      

""" 3. Counts the number of products in each category """

def categories_count(products):
    category_count = {}

    for product in products:
        category = product["category"]

        if category in category_count:
            category_count[category] += 1
        else:
            category_count[category] = 1

    return category_count

category_count = categories_count(products)
print("Product count by category :")
for category, count in category_count.items():
    print(f"{category}: {count} product")


