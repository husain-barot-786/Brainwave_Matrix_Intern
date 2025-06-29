# Python ATM Interface

A simple, fully functional command-line ATM interface written in Python. This project demonstrates user registration, authentication, balance management, and other core banking operations using file-based storage.

---

## Features

- **Register New Account**: Create a new ATM account with your name and a secure 4-digit PIN.
- **Login**: Authenticate using your account number and PIN.
- **Check Balance**: View your current account balance.
- **Deposit Money**: Add funds to your account. Minimum deposit is 1.
- **Withdraw Money**: Withdraw funds, provided you have sufficient balance.
- **Change PIN**: Securely update your PIN.
- **Account Details**: View your account number, name, and balance.
- **Persistent Data**: User data is stored securely in `users.db` (using Python's pickle module).
- **Input Validation**: All user inputs are validated for security and correctness.
- **PIN Security**: PINs are hashed before storing.

---

## Project Structure

```
Python-ATM-Interface/
├── assets/
│   └── demo.mp4
├── atm.py         # Main application file (entry point)
├── database.py    # User database logic
├── user.py        # User account logic
├── utils.py       # Utility functions (hashing, clear screen, etc.)
├── users.db       # Binary file for storing account data (Auto-generated)
├── README.md
├── Report.pdf
└── .gitignore
```

---

## Getting Started

### Requirements

- Python 3.x (no external libraries needed)

### How to Run

1. **Clone or download** the repository and navigate to the project folder.
2. Open a terminal/command prompt in that folder.
3. Run the following command:
    bash
    ```
    python atm.py
    ```

4. Follow the on-screen instructions to register, login, and use ATM features.

---

## Notes

- **Data Persistence**: All accounts and balances are stored in `users.db`. Deleting this file will erase all data.
- **Security**: PINs are stored as secure hashes, not plain text.
- **Minimum Deposit**: The minimum deposit amount is 1. Deposits of 0 or negative numbers are not allowed.
- **Withdrawals**: You cannot withdraw more than your current balance.

---

## Customization

You can add more features such as transaction history, account locking, or even upgrade to a GUI using Tkinter or PyQt.

---

## License

This project is provided for educational purposes and is free to use and modify.

---