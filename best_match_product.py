from products_list import products

def get_best_match(products,target):
    best_match = None
    for product in products:
        if best_match is None or abs(len(product) - len(target)) < abs(len(best_match) - len(target)):
            best_match = product
    return f"Best match product: {best_match}"

search_product = "Printer"
final_result = get_best_match(products,search_product)

print(final_result)

# Product with the closest match to the target 
# Time Complexity:  O(n)
# Space Complexity: O(1)

