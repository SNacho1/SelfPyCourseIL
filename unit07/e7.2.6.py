def print_shopping_list(shopping_list):
    print("the item list is:")
    print(', '.join(shopping_list))

def count_items(shopping_list):
    print("number of item is:", len(shopping_list))

def check_product(shopping_list):
    product_name = input("please enter name of the item:")
    if product_name in shopping_list:
        print("yes, the item is in the list.")
    else:
        print("no, the item isn't in the list.")

def count_specific_product(shopping_list):
    product_name = input("please enter the name of the item to Check how many times is shows:")
    count = shopping_list.count(product_name)
    print("the number of the item is: {}" .format(product_name, count))

def remove_product(shopping_list):
    product_name = input("please enter item name thet you want to remove:")
    if product_name in shopping_list:
     shopping_list.remove(product_name)
     print("the item remove Successfully.")
    else:
     print("cannot be deleted, the item isn't in the list.")

def add_product(shopping_list):
   product_name = input("please enter item name thet you want to add:")
   shopping_list.append(product_name)
   print("the item added Successfully.")

def print_invalid_products(shopping_list):
    invalid_products = [products for products in shopping_list if len(products) < 3 or not products.isalpha()]
    if invalid_products:
       print("the next items is not invalid:")
       print(', '.join(invalid_products))
    else:
       print("there is no invalid items in the list:")

def remove_duplicates(shopping_list):
    unique_list = list(set(shopping_list))
    print("your list after the removing duplicates is:")
    print_shopping_list(unique_list)

def main():
   shopping_list = input("please enter your items list withot comes or profits:").split(',')

   while True:
    print("\menu:")
    print("1: print all your items.")
    print("2: number of items in the list.")
    print("3: to cheek if your item is in the list.")
    print("4: to cheek if your items is showd twice in your list.")
    print("5: to delte item from the list.")
    print("6: to add a item to your list.")
    print("7: to see if your items is invalid.")
    print("8: to remove duplicates")
    print("9: to exit")

    choice = int(input("please pick a number:"))

    if choice == 1:
        print_shopping_list(shopping_list)
    elif choice == 2:
        count_items(shopping_list)
    elif choice == 3:
        check_product(shopping_list)
    elif choice == 4:
        count_specific_product(shopping_list)
    elif choice == 5:
        remove_product(shopping_list)
    elif choice == 6:
        add_product(shopping_list)
    elif choice == 7:
        print_invalid_products(shopping_list)
    elif choice == 8:
        remove_duplicates(shopping_list)
    elif choice == 9:
        break
    else:
        print("your number have to be between 1-9.")

if __name__ == "__main__":
    main()
