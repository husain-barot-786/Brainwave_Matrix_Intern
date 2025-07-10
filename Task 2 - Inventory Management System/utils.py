def is_positive_integer(value):
    try:
        ivalue = int(value)
        return ivalue >= 0
    except ValueError:
        return False

def is_positive_float(value):
    try:
        fvalue = float(value)
        return fvalue >= 0.0
    except ValueError:
        return False

def validate_product_data(pid, name, quantity, price):
    if not pid or not name:
        return False, "Product ID and Name cannot be empty."
    if not is_positive_integer(quantity):
        return False, "Quantity must be a non-negative integer."
    if not is_positive_float(price):
        return False, "Price must be a non-negative number."
    return True, ""