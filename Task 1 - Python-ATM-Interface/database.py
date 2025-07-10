import os
import pickle
from user import User
from utils import hash_pin

class Database:
    def __init__(self, filename):
        self.filename = filename
        self.users = {}
        self.load()

    def load(self):
        if os.path.exists(self.filename):
            with open(self.filename, "rb") as f:
                self.users = pickle.load(f)
        else:
            self.users = {}

    def save(self):
        with open(self.filename, "wb") as f:
            pickle.dump(self.users, f)

    def generate_account_no(self):
        import random
        while True:
            acc_no = str(random.randint(10000000, 99999999))
            if acc_no not in self.users:
                return acc_no

    def create_user(self, name, pin):
        acc_no = self.generate_account_no()
        if acc_no in self.users:
            return None
        user = User(acc_no, name, hash_pin(pin), 0.0)
        self.users[acc_no] = user
        self.save()
        return user

    def authenticate(self, acc_no, pin):
        user = self.users.get(acc_no)
        if user and user.pin_hash == hash_pin(pin):
            return user
        return None

    def update_user(self, user):
        self.users[user.account_no] = user
        self.save()