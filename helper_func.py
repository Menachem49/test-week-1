from crod_json import load_orderes


def is_the_order_exist(order_id):
    orders = load_orderes()
    f = filter(lambda o:o["id"]==order_id , orders)
    if f:
        return True
    return False
def is_the_prodict_exsit(product_id, productes):
    return filter(lambda p :p["id"] == product_id, productes)

def is_digit(value):
    try:
        return int(value) and not isinstance(value, bool)
        
    except ValueError:
        return False

def is_postive(value):
    return int(value) > 0

def is_digit_in_range(value, min, max):
    return int(value) in range(min, max + 1)


