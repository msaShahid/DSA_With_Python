def search_product(product_list, target_product):
    product_list.sort()
    left, right = 0, len(product_list) - 1

    while left <= right:
        mid = (left + right) // 2
        if product_list[mid] == target_product:
            return f"Product is available : {product_list[mid]}"
        elif product_list[mid] < target_product:
            left = mid + 1
        else:
            right = mid - 1
    return f"Product is not available : {target_product}"

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
    "Camera",
    "Printer",
    "Scanner",
    "Webcam",
    "Projector",
    "External Hard Drive",
    "USB Flash Drive",
    "Graphics Card",
    "Power Bank",
    "Router",
    "Smart TV"
]

desired_product = "Router"
search_result = search_product(product_list, desired_product)
print(search_result)


# Binary search algorithm is much faster than a linear search.
# Time Complexity: O(log n)
# Space Complexity: O(1)