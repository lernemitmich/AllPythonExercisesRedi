restaurants = []

while True:
    print("Choose an option:")
    print("a. Add a restaurant")
    print("b. Remove a restaurant")
    print("c. Show all restaurants")
    print("d. Exit the program")

    choice = input("Enter your choice: ")

    if choice == "a":
        restaurant = input("Enter the name of the restaurant to add: ")
        restaurants.append(restaurant)
        print("Restaurant added successfully.")

    elif choice == "b":
        restaurant = input("Enter the name of the restaurant to remove: ")
        if restaurant in restaurants:
            restaurants.remove(restaurant)
            print("Restaurant removed successfully.")
        else:
            print("Restaurant not found in the list.")

    elif choice == "c":
        print("List of restaurants:")
        for restaurant in restaurants:
            print(restaurant)

    elif choice == "d":
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please try again.")
