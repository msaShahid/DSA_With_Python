from products_list import products

def bubble_sort(products):
    n = len(products)
    for i in range(n):
        for j in range(0, n - i - 1):
            if products[j]['price'] > products[j + 1]['price']:
                """
                    If the price of the product at index j is greater than the price of the product at index j + 1 then
                    the two products are swapped. = T
                """
                products[j], products[j + 1] = products[j + 1], products[j]
                """
                    if the above condition is True (T), Swapping ensures the larger price moves up towards the end of the list.
                """
    return products

final_result = bubble_sort(products)

""" 
Product list of dictionaries is sorted by price
Time Complexity = O(n2)
Space Complexity = O(1)

"""

for items in final_result:
    print(f"{items['name']} with a price of ${items['price']}")



