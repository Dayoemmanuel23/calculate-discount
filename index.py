# Function to calculate discount
def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying discount.
    If discount is 20% or higher, applies discount.
    Otherwise, returns the original price.
    """
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price


# Prompt the user for inputs
price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Use the function
final_price = calculate_discount(price, discount_percent)

# Print results
if discount_percent >= 20:
    print(f"Discount applied! Final price: {final_price}")
else:
    print(f"No discount applied. Price remains: {final_price}")
