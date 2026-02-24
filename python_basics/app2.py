import tkinter as tk
from tkinter import messagebox

# ----------------------------
# Product Price List
# ----------------------------
products = {
    "Bread": 60,
    "Milk": 70,
    "Sugar": 150,
    "Rice": 120,
    "Soap": 80
}

cart = []

# ----------------------------
# Add Item
# ----------------------------
def add_item():
    name = product_var.get()
    qty = qty_entry.get()

    if name == "" or qty == "":
        messagebox.showwarning("Warning", "Select product and quantity")
        return

    qty = int(qty)
    price = products[name]
    total = price * qty

    cart.append((name, qty, total))
    receipt.insert(tk.END, f"{name} x{qty} = Ksh {total}\n")
    update_total()

# ----------------------------
# Update Total
# ----------------------------
def update_total():
    total = sum(item[2] for item in cart)
    total_label.config(text=f"Total: Ksh {total}")

# ----------------------------
# Clear Cart
# ----------------------------
def clear_cart():
    cart.clear()
    receipt.delete(1.0, tk.END)
    total_label.config(text="Total: Ksh 0")

# ----------------------------
# Exit App
# ----------------------------
def exit_app():
    root.destroy()

# ----------------------------
# GUI Window
# ----------------------------
root = tk.Tk()
root.title("Supermarket POS")
root.geometry("500x500")

tk.Label(root, text="Supermarket POS", font=("Arial", 20)).pack()

# Product Dropdown
product_var = tk.StringVar()
tk.Label(root, text="Select Product").pack()
tk.OptionMenu(root, product_var, *products.keys()).pack()

# Quantity
tk.Label(root, text="Quantity").pack()
qty_entry = tk.Entry(root)
qty_entry.pack()

# Buttons
tk.Button(root, text="Add Item", command=add_item).pack(pady=5)
tk.Button(root, text="Clear Cart", command=clear_cart).pack(pady=5)
tk.Button(root, text="Exit", command=exit_app).pack(pady=5)

# Receipt
receipt = tk.Text(root, height=15)
receipt.pack()

# Total
total_label = tk.Label(root, text="Total: Ksh 0", font=("Arial", 14))
total_label.pack()

root.mainloop()