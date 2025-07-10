class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password  # For demo; use hashed passwords in production.

class UserManager:
    def __init__(self):
        self.users = {}

    def add_user(self, user):
        self.users[user.username] = user

    def authenticate(self, username, password):
        user = self.users.get(username)
        if user and user.password == password:
            return True
        return False