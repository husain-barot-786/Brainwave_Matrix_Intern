from inventory import Inventory

class ReportGenerator:
    def __init__(self, inventory: Inventory):
        self.inventory = inventory

    def low_stock_report(self, threshold=5):
        low_stock = self.inventory.get_low_stock(threshold)
        if not low_stock:
            return "All products are sufficiently stocked."
        report = f"Low Stock Products (Threshold: {threshold}):\n"
        report += "-"*95 + "\n"
        report += "{:<15}{:<20}{:<15}{:<20}{:<15}\n".format("Product ID", "Product Name", "Quantity", "Price per Unit", "Total Value")
        report += "-"*95 + "\n"
        for prod in low_stock:
            total_value = prod.quantity * prod.price
            report += "{:<15}{:<25}{:<15}{:<15.2f}{:<15.2f}\n".format(
                prod.pid, prod.name, prod.quantity, prod.price, total_value)
        return report

    def sales_summary_report(self):
        products = self.inventory.get_all_products()
        if not products:
            return "No products in inventory."
        report = "Sales Summary Report:\n"
        report += "-"*95 + "\n"
        report += "{:<15}{:<20}{:<15}{:<20}{:<20}\n".format(
            "Product ID", "Product Name", "Quantity", "Price per Unit", "Total Inventory Value"
        )
        report += "-"*95 + "\n"
        total_value = 0
        for prod in products:
            prod_total = prod.quantity * prod.price
            report += "{:<15}{:<25}{:<15}{:<20.2f}{:<15.2f}\n".format(
                prod.pid, prod.name, prod.quantity, prod.price, prod_total
            )
            total_value += prod_total
        report += "-"*95 + f"\nTotal Inventory Value: {total_value:.2f}\n"
        return report