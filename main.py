from menu import print_menu
from orders_func import create_order, show_all_orders, find_order_by_id, close_order
from helper_func import is_digit_in_range


if __name__ == "__main__":
    
    FUNC = {
         "1": create_order,
         "2": show_all_orders,
         "3": find_order_by_id,
         "4": close_order,
        #  "5": show_sales_report
    }

    KEY_IN_DICT_FUNC = (0,5)  

    choice = ''

    while True :
        print_menu()
        while True:
            try:
                choice = int(input().strip())
                if is_digit_in_range(choice, *KEY_IN_DICT_FUNC):
                    break
                print("Enter a number bitwien 1 - 5")
            except ValueError:
                print("Enter only numbers!")
        if choice == 0:
            break
        print(FUNC[str(choice)]())

