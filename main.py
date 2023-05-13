
def decimal_to_hex(decimal):
    return hex(decimal)[2:]

def hex_to_decimal(hexadecimal):
    return int(hexadecimal, 16)

def decimal_to_binary(decimal):
    return bin(decimal)[2:]

def binary_to_decimal(binary):
    return int(binary, 2)

def hex_to_binary(hexadecimal):
    decimal = hex_to_decimal(hexadecimal)
    return decimal_to_binary(decimal)

def binary_to_hex(binary):
    decimal = binary_to_decimal(binary)
    return decimal_to_hex(decimal)

def print_menu():
    print("Please select an option:")
    print("1. Convert from decimal to hexadecimal")
    print("2. Convert from hexadecimal to decimal")
    print("3. Convert from decimal to binary")
    print("4. Convert from binary to decimal")
    print("5. Convert from hexadecimal to binary")
    print("6. Convert from binary to hexadecimal")
    print("0. Exit")

def main():
    while True:
        print_menu()
        option = int(input("Enter your choice (0-6): "))

        if option == 0:
            print("Exiting the program...")
            break

        if option == 1:
            decimal = int(input("Enter the decimal number: "))
            hexadecimal = decimal_to_hex(decimal)
            print("Hexadecimal: " + hexadecimal)
        elif option == 2:
            hexadecimal = input("Enter the hexadecimal number: ")
            decimal = hex_to_decimal(hexadecimal)
            print("Decimal: " + str(decimal))
        elif option == 3:
            decimal = int(input("Enter the decimal number: "))
            binary = decimal_to_binary(decimal)
            print("Binary: " + binary)
        elif option == 4:
            binary = input("Enter the binary number: ")
            decimal = binary_to_decimal(binary)
            print("Decimal: " + str(decimal))
        elif option == 5:
            hexadecimal = input("Enter the hexadecimal number: ")
            binary = hex_to_binary(hexadecimal)
            print("Binary: " + binary)
        elif option == 6:
            binary = input("Enter the binary number: ")
            hexadecimal = binary_to_hex(binary)
            print("Hexadecimal: " + hexadecimal)
        else:
            print("Invalid option. Please try again.")

        print()  # Print an empty line for separation

main()