# William Sumrall
# ITEC 1250
# Chapter 5, Challenge 3
# Who's Your Daddy Program

father_son = {"Matt" : "William",
              "Ben" : "William",
              "Jack": "Peter",
              "Jude": "Bill",
              "Thomas": "Jackson"}

choice = None
while choice != 5:
    print(
    """
    Option Menu:

    1 - Who's the daddy
    2 - Remove son-father pair
    3 - Add son-father pair
    4 - Replace father
    5 - Quit

    """)

    choice = int(input("Choice: "))
    
    if choice == 1:
        son = input("\nEnter name of son: ")
        if son in father_son:
            print("\nYour father is", father_son[son])
        else:
            print("\nSorry, son doesn't exist in the dictionary.")

    elif choice == 2:
        son = input("\nEnter name of son: ")
        if son in father_son:
            del father_son[son]
            print("\nfather-son pair has been removed from the dictionary.")
        else:
            print("\nSorry, son doesn't exist in the dictionary.")

    elif choice == 3:
        son = input("\nEnter name of son: ")
        father = input("\nEnter name of father: ")
        if not(son) in father_son:
            father_son[son] = father
            print("\nSon and father pair is added.")
        else:
            print("\nSorry, father-son pair already exist in the dictionary.")

    elif choice == 4:
        son = input("\nEnter name of son you want to replace: ")
        if son in father_son:
            father = input("\nEnter name of father you want to replace: ")
            father_son[son] = father
            print("\n", son, "Son and father pair is replaced.")
        else:
            print("\nSorry, father-son pair doesn't exist in the dictionary.")

input("\nPress enter to exit.")
