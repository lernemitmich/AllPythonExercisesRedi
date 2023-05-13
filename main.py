#Print to the user: “Welcome to the game”
print("Welcome to the game")

#Ask the user if they want to search the treasure a. at the beach or b. in the mountains

answer = input("Do you want to search the treasure:\n a. at the beach\n b. in the mountains\n")

if answer == "a":
    option_a = input("Do you want to search:\n 1. in the water\n 2. dig a hole in the sand\n")
    if option_a == "1":
        # Code for searching in the water
        print("You have chosen to search in the water.")
        print("Unfortunately, you didn't find the treasure, but you found an old stinky shoe.")
    elif option_a == "2":
        # Code for digging a hole in the sand
        print("You have chosen to dig a hole in the sand.")
        print("Congratulations! You found a treasure box with gold!")
    else:
        print("Invalid option.")
elif answer == "b":
    option_b = input("Do you want to search:\n 3. under a palm tree\n 4. in a lake\n")
    if option_b == "3":
        # Code for searching under a palm tree
        print("You have chosen to search under a palm tree.")
        print("Unfortunately, you got bit by a snake and lost.")
    elif option_b == "4":
        # Code for searching in a lake
        print("You have chosen to search in a lake.")
        print("You found a treasure box underwater, but it's empty.")
    else:
        print("Invalid option.")
else:
    print("Invalid option.")
