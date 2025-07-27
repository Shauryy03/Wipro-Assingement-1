# Supermarket Billing Analysis

try:
    filename = input("Enter the file name: ")
    with open(filename + ".txt", "r") as file:
        lines = file.readlines()

    items_purchased = 0
    free_items = 0
    total_amount = 0
    discount = 0

    for line in lines:
        line = line.strip()
        if not line:
            continue  # Skip blank lines

        parts = line.split()
        if len(parts) != 2:
            continue  # Skip malformed lines

        item, value = parts
        if item.lower() == "discount":
            try:
                discount = int(value)
            except ValueError:
                print("Invalid discount value.")
        elif value.lower() == "free":
            free_items += 1
        else:
            try:
                price = int(value)
                total_amount += price
                items_purchased += 1
            except ValueError:
                print(f"Invalid price for item: {item}")

    final_amount = total_amount - discount

    print("No of items purchased:", items_purchased)
    print("No of free items:", free_items)
    print("Amount to pay:", total_amount)
    print("Discount given:", discount)
    print("Final amount paid:", final_amount)

except FileNotFoundError:
    print("File not found. Please check the filename and try again.")
except Exception as e:
    print("An error occurred:", e)
