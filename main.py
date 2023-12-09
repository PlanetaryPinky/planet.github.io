import tkinter as tk
from tkinter import ttk

# Define the food items and their prices
food_items = {
    "Pizza Slice": 1.99,
    "Ice Cream Cup": 1.99,
    "Soda": 0.69,
    "Churro": 1.49,
    "Pizza": 9.95,
    "Hot dog and Drink Combo": 1.49,
    "Roast Beef Sandwich": 9.99,
    "Chicken Bake": 3.99
}

# Define the tax rate
TAX_RATE = 0.04

# This is a function to simulate adding items to the order
def add_item(item_name, price):
    order_listbox.insert(tk.END, f"{item_name} - ${price:.2f}")
    update_total(price)

# Function to update the total
def update_total(price):
    global subtotal
    subtotal += price
    tax = subtotal * TAX_RATE
    total = subtotal + tax
    subtotal_var.set(f"Subtotal: ${subtotal:.2f}")
    tax_var.set(f"Tax: ${tax:.2f}")
    total_var.set(f"Total: ${total:.2f}")

# Function to reset the order
def reset_order():
    global subtotal
    subtotal = 0.0
    subtotal_var.set(f"Subtotal: ${subtotal:.2f}")
    tax_var.set(f"Tax: $0.00")
    total_var.set(f"Total: $0.00")
    order_listbox.delete(0, tk.END)

# Initialize the subtotal
subtotal = 0.0

# Create the main window
root = tk.Tk()
root.title("Costco Food Order")

# Define variables for the subtotal, tax, and total
subtotal_var = tk.StringVar(value=f"Subtotal: ${subtotal:.2f}")
tax_var = tk.StringVar(value="Tax: $0.00")
total_var = tk.StringVar(value="Total: $0.00")

# Create frames for the menu and the order summary
menu_frame = tk.Frame(root, bg='lightgrey', width=300)
order_frame = tk.Frame(root, bg='white')

menu_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
order_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# In the menu frame, create buttons for the food items
for food, price in food_items.items():
    button = tk.Button(menu_frame, text=f"{food} - ${price}", command=lambda f=food, p=price: add_item(f, p))
    button.pack(pady=2, padx=5, fill=tk.X)

# In the order frame, create a listbox to display the order items
order_listbox = tk.Listbox(order_frame)
order_listbox.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# Labels for the subtotal, tax, and total
subtotal_label = tk.Label(order_frame, textvariable=subtotal_var, font=('Arial', 16))
subtotal_label.pack(side=tk.TOP, fill=tk.X)
tax_label = tk.Label(order_frame, textvariable=tax_var, font=('Arial', 16))
tax_label.pack(side=tk.TOP, fill=tk.X)
total_label = tk.Label(order_frame, textvariable=total_var, font=('Arial', 16))
total_label.pack(side=tk.TOP, fill=tk.X)

# Reset button
reset_button = tk.Button(order_frame, text="Reset", command=reset_order)
reset_button.pack(side=tk.BOTTOM, fill=tk.X)

# Start the main loop
root.mainloop()
