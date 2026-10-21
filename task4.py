raw_delivery = [
    ("Apple", 0.75, 50),
    ("Banana", 0.40, 100),
    ("Milk", 2.50, 15),
    ("Bread", 1.80, 20),
    ("Apple", 0.75, 30),  ]

shopping_cart = ["Apple", "Apple", "Milk", "Dragonfruit", "Bread"]

def build_inventory(raw_delivery):
    inventory={}
    for product,price,quantity in raw_delivery:
        if product in inventory:
            inventory[product]["stock"]+=quantity
        else:
            inventory[product]={
                "price":price,
                "stock":quantity
            }
    return inventory

def process_cart(inventory,shopping_card):
    receipt=[]
    for product in shopping_card:
        if product not in inventory:
            print(f"{product} is not carried in this store")

        elif inventory[product]["stock"] <= 0:
            print(f"{product} is sold out!")

        else:
            price = inventory[product]["price"]
            inventory[product]["stock"] -= 1

            receipt.append((product, inventory[product]["price"]))

    return receipt

inventory = build_inventory(raw_delivery)

receipt = process_cart(inventory, shopping_cart)

print("\n-------RECEIPT-------")

total=0
for product, price in receipt:
    print(f"{product}          :${price:.2f}")
    
    
    total +=     price 
    print(f"Total price    :${total:.2f}\n")