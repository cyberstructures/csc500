# Spencer Ingram CSC500 - Professor Dr. Joseph Issa
# Portfolio milestone module 2.
# Initialization of variables and functions for the portfolio project.


# class definitions for item and cart
class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def total_cost(self):
        return sum(item.total_price() for item in self.items)


class ShoppingCartItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_price(self):
        return self.price * self.quantity


cart = ShoppingCart()
keep_shopping = "y"

print("Time to go shopping!")
while keep_shopping == "y":
    itemname = input(
        "Type your next item to add to your shopping cart and press enter."
    )
    itemprice = float(input("Type the price per item and press enter."))
    itemquantity = int(input("Type the quantity of items and press enter."))
    item = ShoppingCartItem(itemname, itemprice, itemquantity)
    cart.add_item(item)
    print(f"You have added {itemquantity} {itemname}(s) to your shopping cart.")
    print(f"Your current total is: ${cart.total_cost():.2f}")
    print(f"Your current shopping cart contains:")
    for i, item in enumerate(cart.items, start=1):
        print(f"{i}. {item.quantity} x {item.name} = ${item.total_price():.2f}")
    print("--------------------------------------------------")
    keep_shopping = input("Do you want to add another item? (y/n): ")
print(f"All done. Your final total is: ${cart.total_cost():.2f}")
print("Thanks for shopping your business!")
