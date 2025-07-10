from user import User, UserManager

user_manager = UserManager()
user_manager.add_user(User("admin", "admin123"))  # Default admin

def login(username, password):
    return user_manager.authenticate(username, password)