# Name my list
name_of_list = input("Hi 🥳 Name your list 👉 ")


# Gather user's choice


# list before alterations (0 items)
list_of_groceries = []


while True:
    choice = input('Choose an Option\n[A]to Add Itens\n[D]to Delete an item\n[S]to See full list:\n').lower()
    
    if choice == 'a':
        new_item = input('\nEnter new item: ')
        list_of_groceries.append(new_item)
        print(f'\n{new_item} added to the list!\n')


        leave_or_continue = input("Do you want to keep adding? [Y]es or N[o] ").lower()
            if leave_or_continue == 'Y'
                continue
            else:
                break

    elif choice == 'd':

        continue

    elif choice == 'b':

        deleted_item = input('Item to delete: ')
        if deleted_item in list_of_groceries:

            list_of_groceries.remove(deleted_item)
            print(f'{deleted_item} deleted from the list\n')

        else: 
            print(f'{deleted_item} not in list.\n')

    

    elif choice == 'v':
        
        for i, item in enumerate(list_of_groceries, start = 1):
            print(i, item)

    else:
        print("Choice not available. Please, enter another answer 😊\n")

    elif choice == 'c':
        
        for i, item in enumerate(list_of_groceries):
            print(i, item)

    else:
        print("Choice not available. Please, enter another answer 😊")

        continue
        