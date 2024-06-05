def add_item_to_list(my_list):
    item = input("Enter an item to add to the list: ")
    my_list.append(item)

def remove_item_from_list(my_list):
    item = input("Enter an item to remove from the list: ")
    if item in my_list:
        my_list.remove(item)
    else:
        print("Item not found in the list.")

my_list = []
add_item_to_list(my_list)
print(my_list)
remove_item_from_list(my_list)
print(my_list)

def print_list(my_list):
    print("My Grocery List:")
    for item in my_list:
        print(item)
print_list(my_list)