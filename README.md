# Discount Calculator (Python)

This is a simple Python program that calculates the final price of an item after applying a discount.  
The program uses a function `calculate_discount(price, discount_percent)` which only applies the discount if it is **20% or higher**.  
If the discount is less than 20%, the original price is returned.

---

## Features
- Takes the **original price** of an item from the user.
- Takes the **discount percentage** as input.
- Applies the discount only if it is **20% or more**.
- Displays either the **final discounted price** or the **original price**.

---

## How It Works
1. User enters the original price.
2. User enters the discount percentage.
3. The program checks:
   - If discount ≥ 20%, apply discount.
   - Otherwise, keep the price unchanged.
4. The final result is displayed.

---

## Example Usage
```bash
Enter the original price of the item: 100
Enter the discount percentage: 25
Discount applied! Final price: 75.0

## Example Usage
Enter the original price of the item: 100
Enter the discount percentage: 10
No discount applied. Price remains: 100.0

How to Run

Make sure you have Python 3 installed.

Save the code into a file named discount_calculator.py.

Run the program:

