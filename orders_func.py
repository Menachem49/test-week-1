from helper_func import is_digit, is_the_prodict_exsit, is_postive, is_digit_in_range, is_the_order_exist
from crod_json import load_orderes, save_orderes


DISCOUNT_UP_TO_700 = 5
DISCOUNT_UP_TO_1500 = 10
DISCOUNT_FROM_1500 = 15
PRODUCTS = [
    {"id": 1, "name": "Keyboard", "price": 120},
    {"id": 2, "name": "Mouse", "price": 80},
    {"id": 3, "name": "Monitor", "price": 900},
    {"id": 4, "name": "Headphones", "price": 200},
    {"id": 5, "name": "USB Cable", "price": 30}
]

def receiving_an_order():
   
    items = []
    choice = ''
    while True and choice != 0:
        while True:
            try:
                product_id = int(input("Entet the product id: ").strip())
                if is_the_prodict_exsit(product_id, PRODUCTS):
                    break
                print("product id is not found")
            except ValueError:
                print("Enter omly numbers!")

        while True:
            try:
                quantity = int(input("Enter amount: ").strip())
                
                if is_postive(quantity):
                    break
                print("amount cen not be smuler tehn 1")
                
            except ValueError:
                print("Enter omly numbers!")
        product = {"product_id": int(product_id), "quantity": int(quantity)}
        items.append(product)
        while True :
            if choice == 0:
                break
            RANGE = (0,1)
            try:
                choice = int(input("To enter more products preess 1 to finish preess 0: ").strip())
                if is_digit_in_range(choice, *RANGE):
                    break
                print('Enter only 1 or 0')
            except ValueError:
                print("Enter omly numbers!")
    return items
    
def find_price_by_id(id_):
    for p in PRODUCTS:
        if p["id"] == id_:
            return p["price"]
        
def price_calculation(items: list ):
    total = 0
    for item in items:
        total += item["quantity"] * find_price_by_id(item["product_id"])
    if total < 300:
        return [total, total, 0]
    if total < 700:
        return [total, total * ((100 - DISCOUNT_UP_TO_700) / 100), DISCOUNT_UP_TO_700]
    if total < 1500:
        return [total, total * ((100 - DISCOUNT_UP_TO_1500) / 100), DISCOUNT_UP_TO_1500]
    return [total, total * ((100 - DISCOUNT_FROM_1500) / 100), DISCOUNT_FROM_1500]

def crate_order_id():
    return len(load_orderes())+1

def create_order():
    orderes = load_orderes()
    id_ = crate_order_id()
    items = receiving_an_order()
    price = price_calculation(items)
    order = {
    "id": id_,
    "items": items,
    "total": price[1],
    "status": "OPEN"
}
    orderes.append(order)
    save_orderes(orderes)
    return f'''
"id": {id_},
"items": {items},
"total befor dis": {price[0]},
"final price: : {price[1]}
"percentages" {price[2]}%
    '''

def show_all_orders():
    strem = ""
    orders = load_orderes()
    if not orders:
        return strem
    
    return orders

def find_order_by_id():
    while True:
        try:
            order_id = int(input("Enter order id: ").strip())
            if is_the_order_exist(order_id):
                break
            print("Order id is not found")
        except ValueError:
            print("Enter only numbers!")
    orders = load_orderes()
    order_find = list(filter(lambda o:o["id"]==order_id , orders))
    return order_find

def close_order():
    while True:
        try:
            order_id = int(input("Enter order id: ").strip())
            if is_the_order_exist(order_id):
                break
            print("Order id is not found")
        except ValueError:
            print("Enter only numbers!")
    
    
    # new_order = {
    #     "id": order["id"],
    #     "items": order["items"],
    #     "total": order["total"],
    #     "status": "CLOSED"
    # }
    orders = load_orderes()
    for order in orders:
        if order["id"] == order_id:
            if order["status"] == "CLOSED":
                return "order is alredy exist"
            order["status"] = "CLOSED"
    save_orderes(orders)
    return 'clossed successfully'

    
    


