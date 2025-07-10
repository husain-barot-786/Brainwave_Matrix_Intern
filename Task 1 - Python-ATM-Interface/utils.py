import os
import hashlib

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def pause():
    input("\nPress Enter to continue...")

def hash_pin(pin):
    return hashlib.sha256(pin.encode()).hexdigest()