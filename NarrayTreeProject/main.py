from n_array import NArray
from exceptions import TreeError


def menu():
    """
    Present a menu for interacting with an array tree.

    Options:
        1. Create an array tree.
        2. Insert a value.
        3. Delete a value.
        4. Print the tree.
        5. Exit.
    """
    array_tree = None
    while True:
        choice = input('Please enter your choice:\n'
                       '1. Create an array tree.\n'
                       '2. Insert a value.\n'
                       '3. Delete a value.\n'
                       '4. Print the tree.\n'
                       '5. Exit.\n')
        if choice == '1':
            entry = int(input('Enter an entry in order to create an array tree.\n'))
            array_tree = NArray(entry)
        elif choice == '2':
            try:
                if array_tree is None:
                    raise UnboundLocalError("Invalid choice, please try again.")
                value = int(input('Enter a value to insert to the array tree.\n'))
                array_tree.insert(value)
            except UnboundLocalError as e:
                print(e)
        elif choice == '3':
            try:
                if array_tree is None:
                    raise UnboundLocalError("Invalid choice, please try again.")
                value = int(input('Enter a value to delete from the array tree.\n'))
                array_tree.delete(value)
            except UnboundLocalError as e:
                print(e)
            except TreeError as e:
                e.handel()
                print(array_tree)
        elif choice == '4':
            print(array_tree)
        elif choice == '5':
            return
        else:
            print('Invalid choice, please try again.')


if __name__ == '__main__':
    menu()
