class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"({self.name}, ${self.price})"
    
def inseration_sort(cart):
    for i in range(1, len(cart)):
        current_item = cart[i]
        j = i - 1
        while j >= 0 and cart[j].price > current_item.price:
            cart[j + 1] = cart[j]
            j -= 1
        cart[j + 1] = current_item

cart = []

cart.append(Item("Laptop",1299))
cart.append(Item("Phone", 599))
cart.append(Item("Tablet", 799))
inseration_sort(cart)

for item in cart:
    print(item)
