# define cart function 
def cart_items(cart):
    total_items_cost = 0

    for item in cart:
        total_items_cost += item['Price'] * item['quantity']

    return total_items_cost

# example of cart

cart = [
    {'name' : 'apple', 'Price': 100, 'quantity': 6},
    {'name' : 'banana', 'Price': 60, 'quantity': 12},
    {'name' : 'Guava', 'Price': 80, 'quantity': 3},
    {'name' : 'Mango', 'Price': 300, 'quantity': 12}
]

# Calling function
obj = cart_items(cart)
print(obj)


