class Product:
    def __init__(self, pid, name, quantity, price):
        self.pid = pid
        self.name = name
        self.quantity = quantity
        self.price = price

class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        self.products[product.pid] = product

    def edit_product(self, pid, name=None, quantity=None, price=None):
        if pid in self.products:
            if name is not None:
                self.products[pid].name = name
            if quantity is not None:
                self.products[pid].quantity = quantity
            if price is not None:
                self.products[pid].price = price

    def delete_product(self, pid):
        if pid in self.products:
            del self.products[pid]

    def get_product(self, pid):
        return self.products.get(pid, None)

    def get_low_stock(self, threshold=5):
        return [p for p in self.products.values() if p.quantity <= threshold]

    def get_all_products(self):
        return list(self.products.values())

    def get_sales_summary(self):
        total_value = 0
        for p in self.products.values():
            total_value += p.price * p.quantity
        return total_value