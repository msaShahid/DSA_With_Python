from products_list import products


def similar_product_search(products):
    similar_product = []
    for p1 in range(len(products)):
        for p2 in range(p1 + 1, len(products)):
            if products[p1]['name'][0].lower() == products[p2]['name'][0].lower():
                similar_product.append((products[p1]['name'], products[p2]['name']))
    return similar_product

final_result = similar_product_search(products)

print("-- Similar Products list --")
for pair in final_result:
    print(pair)

# Nested Loops
# Time Complexity:  O(n2)
# Space Complexity: O(n2)