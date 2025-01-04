def product_seacrh(product_list, target_product):
    for product in product_list:
        if product == target_product:
            return product
    return None
    
product_list = [
    "Laptop",
    "Smartphone",
    "Tablet",
    "Smartwatch",
    "Headphones",
    "Keyboard",
    "Mouse",
    "Monitor",
    "Speaker",
    "Camera"
]

target_product = "Tablet"

find_result = product_seacrh(product_list, target_product)

print(find_result)  

# This function iterates through the list product_list to find the target_product
# Time Complexity = O(n)
# Space Complexity = O(1)