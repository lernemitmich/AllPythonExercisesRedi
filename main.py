exchange_rates = {
    "Ghana Cedi": 12.94,
    "Mexican Peso": 19.84,
    "Nigerian Naira": 507.08,
    "Swiss Franc": 0.98,
    "US Dollar": 0.91,
}


currency = input("Enter the currency you want to convert to: ")
amount = float(input("Enter the amount in euros you want to convert: "))

currency = currency.strip().title()  # Remove leading/trailing spaces and convert to title case

if currency in exchange_rates:
    conversion_rate = exchange_rates[currency]
    converted_amount = amount * conversion_rate
    print(f"You would receive {converted_amount} {currency}.")
else:
    print("Currency not found in the exchange rates.")