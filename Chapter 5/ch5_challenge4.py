# William Sumrall
# ITEC 1250
# Chapter 5, Challenge 4
# Who's Your Daddy V2 Program

father_son = {"Matt" : ["William", "Louis"],
              "Jack" : ["Peter", "John"]}

choice = None
while choice != 7:
    print(
    """
    Option Menu:

    1 - Who's the daddy
    2 - Who's the grandfather
    3 - Remove son-father-grandfather pair
    4 - Add son-father-grandfather pair
    5 - Replace father
    6 - Replace grandfather
    7 - Quit

    """)

    choice = int(input("Choice: "))
    
    if choice == 1:
        son = input("\nEnter name of son: ")
        if son in father_son:
            print("\nYour father is", father_son[son][0])
        else:
            print("\nSorry, son doesn't exist in the dictionary.")

    elif choice == 2:
        son = input("\nEnter name of son: ")
        if son in father_son:
            print("\nYour grandfather is", father_son[son][1])
        else:
            print("\nSorry, son doesn't exist in the dictionary.")

    elif choice == 3:
        son = input("\nEnter name of son: ")
        if son in father_son:
            del father_son[son]
            print("\nfather, son and grandfather pair has been removed from the dictionary.")
        else:
            print("\nSorry, son doesn't exist in the dictionary.")

    elif choice == 4:
        son = input("\nEnter name of son: ")
        father = input("\nEnter name of father: ")
        grandfather = input("\nEnter name of granfather: ")
        if not(son) in father_son:
            father_son[son] = [father, grandfather]
            print("\nSon, father and grandfather pair is added.")
        else:
            print("\nSorry, father, son and grandfather pair already exist in the dictionary.")

    elif choice == 5:
        son = input("\nEnter name of son you want to replace: ")
        if son in father_son:
            father = input("\nEnter name of father you want to replace: ")
            father_son[son][0] = father
            print("\n", son, "Son and father pair is replaced.")
        else:
            print("\nSorry, father and son pair doesn't exist in the dictionary.")

    elif choice == 6:
        son = input("\nEnter name of son you want to replace: ")
        if son in father_son:
            father = input("\nEnter name of father you want to replace: ")
            father_son[son][1] = grandfather
            print("\n", son, "Son and grandfather pair is replaced.")
        else:
            print("\nSorry, son and grandfather pair doesn't exist in the dictionary.")

input("\nPress enter to exit.")
