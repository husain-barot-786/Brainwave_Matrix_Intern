import tkinter as tk
from tkinter import messagebox, simpledialog
from inventory import Inventory, Product
from auth import login
from reports import ReportGenerator
from utils import validate_product_data

class InventoryApp:
    def __init__(self):
        self.inventory = Inventory()
        self.report_gen = ReportGenerator(self.inventory)
        self.root = tk.Tk()
        self.root.title("Inventory Management System")
        self.logged_in = False

    def run(self):
        self.login_screen()
        self.root.mainloop()

    def login_screen(self):
        self.clear()
        tk.Label(self.root, text="Username").pack()
        username_entry = tk.Entry(self.root)
        username_entry.pack()
        tk.Label(self.root, text="Password").pack()
        password_entry = tk.Entry(self.root, show="*")
        password_entry.pack()
        def attempt_login():
            if login(username_entry.get(), password_entry.get()):
                self.logged_in = True
                self.main_menu()
            else:
                messagebox.showerror("Login Failed", "Invalid credentials")
        tk.Button(self.root, text="Login", command=attempt_login).pack()

    def main_menu(self):
        self.clear()
        tk.Label(self.root, text="Inventory Management System", font=("Arial", 14)).pack(pady=10)
        tk.Button(self.root, text="Add Product", width=25, command=self.add_product_screen).pack(pady=2)
        tk.Button(self.root, text="View Product Inventory", width=25, command=self.view_products_screen).pack(pady=2)
        tk.Button(self.root, text="Low Stock Report", width=25, command=self.low_stock_report_screen).pack(pady=2)
        tk.Button(self.root, text="Sales Summary Report", width=25, command=self.sales_summary_report_screen).pack(pady=2)
        tk.Button(self.root, text="Exit", width=25, command=self.root.quit).pack(pady=10)

    def add_product_screen(self):
        self.clear()
        tk.Label(self.root, text="Add New Product", font=("Arial", 12, "bold")).pack(pady=5)
        tk.Label(self.root, text="Product ID").pack()
        pid_entry = tk.Entry(self.root)
        pid_entry.pack()
        tk.Label(self.root, text="Product Name").pack()
        name_entry = tk.Entry(self.root)
        name_entry.pack()
        tk.Label(self.root, text="Quantity").pack()
        quantity_entry = tk.Entry(self.root)
        quantity_entry.pack()
        tk.Label(self.root, text="Price per Unit").pack()
        price_entry = tk.Entry(self.root)
        price_entry.pack()

        def add():
            pid = pid_entry.get()
            name = name_entry.get()
            quantity = quantity_entry.get()
            price = price_entry.get()
            valid, msg = validate_product_data(pid, name, quantity, price)
            if not valid:
                messagebox.showerror("Error", msg)
                return
            if self.inventory.get_product(pid):
                messagebox.showerror("Error", "Product ID already exists.")
                return
            self.inventory.add_product(Product(pid, name, int(quantity), float(price)))
            messagebox.showinfo("Success", "Product added.")
            self.main_menu()

        tk.Button(self.root, text="Add Product", command=add).pack(pady=5)
        tk.Button(self.root, text="Back", command=self.main_menu).pack()

    def view_products_screen(self):
        self.clear()
        tk.Label(self.root, text="Product Inventory", font=("Arial", 13, "bold")).pack(pady=5)
        frame = tk.Frame(self.root)
        frame.pack()
        headings = [
            "Product ID", 
            "Product Name", 
            "Quantity", 
            "Price per Unit", 
            "Total Value", 
            "Edit", 
            "Delete"
        ]
        for col, head in enumerate(headings):
            tk.Label(frame, text=head, font=("Arial", 10, "bold"), borderwidth=1, relief="solid", width=15).grid(row=0, column=col)
        for i, prod in enumerate(self.inventory.get_all_products(), start=1):
            total_value = prod.price * prod.quantity
            tk.Label(frame, text=prod.pid, borderwidth=1, relief="solid", width=15).grid(row=i, column=0)
            tk.Label(frame, text=prod.name, borderwidth=1, relief="solid", width=15).grid(row=i, column=1)
            tk.Label(frame, text=prod.quantity, borderwidth=1, relief="solid", width=15).grid(row=i, column=2)
            tk.Label(frame, text=f"{prod.price:.2f}", borderwidth=1, relief="solid", width=15).grid(row=i, column=3)
            tk.Label(frame, text=f"{total_value:.2f}", borderwidth=1, relief="solid", width=15).grid(row=i, column=4)
            tk.Button(frame, text="Edit", command=lambda pid=prod.pid: self.edit_product_screen(pid)).grid(row=i, column=5)
            tk.Button(frame, text="Delete", command=lambda pid=prod.pid: self.delete_product(pid)).grid(row=i, column=6)
        tk.Button(self.root, text="Back", command=self.main_menu).pack(pady=5)

    def edit_product_screen(self, pid):
        product = self.inventory.get_product(pid)
        if not product:
            messagebox.showerror("Error", "Product not found.")
            return
        self.clear()
        tk.Label(self.root, text="Edit Product", font=("Arial", 12, "bold")).pack(pady=5)
        tk.Label(self.root, text="Product ID (cannot change)").pack()
        pid_label = tk.Label(self.root, text=product.pid)
        pid_label.pack()
        tk.Label(self.root, text="Product Name").pack()
        name_entry = tk.Entry(self.root)
        name_entry.insert(0, product.name)
        name_entry.pack()
        tk.Label(self.root, text="Quantity").pack()
        quantity_entry = tk.Entry(self.root)
        quantity_entry.insert(0, str(product.quantity))
        quantity_entry.pack()
        tk.Label(self.root, text="Price per Unit").pack()
        price_entry = tk.Entry(self.root)
        price_entry.insert(0, str(product.price))
        price_entry.pack()

        def save():
            name = name_entry.get()
            quantity = quantity_entry.get()
            price = price_entry.get()
            valid, msg = validate_product_data(pid, name, quantity, price)
            if not valid:
                messagebox.showerror("Error", msg)
                return
            self.inventory.edit_product(pid, name, int(quantity), float(price))
            messagebox.showinfo("Success", "Product updated.")
            self.view_products_screen()

        tk.Button(self.root, text="Save Changes", command=save).pack(pady=5)
        tk.Button(self.root, text="Back", command=self.view_products_screen).pack()

    def delete_product(self, pid):
        if messagebox.askyesno("Confirm Delete", f"Delete product '{pid}'?"):
            self.inventory.delete_product(pid)
            messagebox.showinfo("Deleted", "Product deleted.")
            self.view_products_screen()

    def low_stock_report_screen(self):
        self.clear()
        tk.Label(self.root, text="Low Stock Report", font=("Arial", 12, "bold")).pack(pady=5)
        threshold = simpledialog.askinteger("Low Stock Threshold", "Show products with quantity less than or equal to:", initialvalue=5, minvalue=1)
        if threshold is None:
            self.main_menu()
            return
        report = self.report_gen.low_stock_report(threshold)
        text = tk.Text(self.root, width=95, height=20)
        text.insert("1.0", report)
        text.config(state="disabled")
        text.pack()
        tk.Button(self.root, text="Back", command=self.main_menu).pack(pady=5)

    def sales_summary_report_screen(self):
        self.clear()
        tk.Label(self.root, text="Sales Summary Report", font=("Arial", 12, "bold")).pack(pady=5)
        report = self.report_gen.sales_summary_report()
        text = tk.Text(self.root, width=95, height=20)
        text.insert("1.0", report)
        text.config(state="disabled")
        text.pack()
        tk.Button(self.root, text="Back", command=self.main_menu).pack(pady=5)

    def clear(self):
        for widget in self.root.winfo_children():
            widget.destroy()