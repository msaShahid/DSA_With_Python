from products_list import products

def quick_sort(items):
    if len(items) <= 1:
        return items
    else:
        pivot = items[len(items) // 2]['price']
        left = [x for x in items if x['price'] < pivot]
        middle = [x for x in items if x['price'] == pivot]
        right = [x for x in items if x['price'] > pivot]
        return quick_sort(left) + middle + quick_sort(right)
    
sorted_products = quick_sort(products)

print('Items list : ')
for product in sorted_products:
    print(product['name'], product['price'])
    