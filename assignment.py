store = {
	"laptop": {"price": 1200, "quantity": 5},
	"headphones": {"price": 150, "quantity": 10},
	"mouse": {"price": 40, "quantity": 20}
	}

#high_price = {}
potential_sales = 0	
sold_item = {}

def start():
	while True:
		print("welcome to our online store management system\n1. add a new product\n2. update store product\n3. sell product\n4. display inventory\n5. display most expensive product\n6. total potential sales")
		command = int(input("select an option to continue: "))
		if command == 1:
			add_product()
		elif command == 2:
			update_store()
		elif command == 3:
			sell_product()
		elif command == 4:
			display_inventory()
		elif command == 5:
			expensive_product()
		elif command == 6:
			potential_sale()


def add_product():
	item  = input("enter item name to add: ").lower()
	for items in [store.keys()]:
		if item not in store:
			price = int(input("enter item price: "))
			quantity = int(input("enter item quantity: "))
			store.update({item: {"price": price,
					    "quantity": quantity}
					    })
			print(f"{item} successfully added")
			print(store)

		else:
			print(f"{item} already exist in sore")	

def update_store():
	item  = input("enter item name to update: ").lower()
	for items in [store.keys()]:
		if item in store:
			price = int(input("enter item price: "))
			quantity = int(input("enter item quantity: "))
			store.update({item: {"price": price,
					    "quantity": quantity}
					    })
			print(f"{item} successfully updated")
			print(store)
		else:
			print(f"{item} does not exist in sore")	

def sell_product():
	sold = input("enter a product to sell: ")
	if sold in store:
		qty = int(input("enter quantity for sale: "))
		store[sold]["quantity"] -= qty
		sold_item.update({"item": sold,
				 "quantity": qty})
		print(store)
		print("sold item:", sold_item)
	else:
		print(f"{sold} not in store")
	
def display_inventory():
	for item in store:
		print(item,"price:", store[item]["price"],"quantity:", store[item]["quantity"])

def expensive_product():
	big = 0
	for items in store:
		if store[items]["price"] > big:
			big = store[items]["price"]
			for items in store:
				if store[items]["price"] == big:
					print(f"item: {items}, price: {big}")
			

def potential_sale():
	potential_sales = 0
	for items in store:
		potential_sales += store[items]["price"]
	print("total price of available products: ",potential_sales)






start()
























