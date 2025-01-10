from products_list import products

lowest_price = min(products, key=lambda x: x["price"])

print(f"The lowest price of a product is ${lowest_price['price']} for {lowest_price['name']}")
        
