from products_list import products

def selection_sort(products):
    n = len(products)

    for i in range(n):
        min_index = i
        for j in range(i + 1, n ):
            if products[j]['price'] < products[min_index]['price']:
                min_index = j
        products[i], products[min_index] = products[min_index], products[i]
    return products

final_result = selection_sort(products)
for item in final_result:
    print(item)