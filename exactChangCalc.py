//Working code for coin calc in Python 

def calculate_change(total_change):
    if total_change <= 0:
        return "No change"

    # Coin values in cents
    coin_values = {
        "Dollar": 100,
        "Quarter": 25,
        "Dime": 10,
        "Nickel": 5,
        "Penny": 1
    }

    result = []

    for coin, value in coin_values.items():
        count = total_change // value
        if count > 0:
            # Handle pluralization
            if count == 1:
                coin_name = coin
            else:
                coin_name = f"{coin}s" if coin != "Penny" else "Pennies"
            result.append(f"{count} {coin_name}")
            total_change %= value

    return "\n".join(result)

# Take input
total_change = int(input("Enter the total change amount in cents: "))

# Get the change
change_output = calculate_change(total_change)

# Output the result
print(change_output)
