from utils import hash_pin

class User:
    def __init__(self, account_no, name, pin_hash, balance):
        self.account_no = account_no
        self.name = name
        self.pin_hash = pin_hash
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def deposit(self, amount):
        if amount >= 1:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def change_pin(self, old_pin, new_pin):
        if self.pin_hash == hash_pin(old_pin) and new_pin.isdigit() and len(new_pin) == 4:
            self.pin_hash = hash_pin(new_pin)
            return True
        return False