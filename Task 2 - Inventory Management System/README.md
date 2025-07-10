# Inventory Management System

A simple yet robust Inventory Management System built with Python and Tkinter. This application allows users to manage products, track inventory, generate reports, and perform user authentication within an intuitive graphical interface.

---

## Table of Contents

- [Features](#features)
- [Screenshots](#screenshots)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Installation & Setup](#installation--setup)
- [How to Use](#how-to-use)
- [File Descriptions](#file-descriptions)
- [Data Validation](#data-validation)
- [Extending the Project](#extending-the-project)
- [License](#license)
- [Acknowledgements](#acknowledgements)

---

## Features

- **User Authentication:** Secure login for access control.
- **Product Management:** Add, edit, and delete product records.
- **Inventory Tracking:** View all products with quantity, price, and total value.
- **Reports:** Generate low stock and sales summary reports.
- **Data Validation:** Ensures integrity of all product data entries.
- **Intuitive GUI:** User-friendly interface built with Tkinter.

---

## Screenshots

> Add screenshots of the main interface, product management, and sales summary report here.

---

## Project Structure

```
Inventory-Management-System/
├── assets/
│   └── demo.mp4
├── main.py             # Application entry point
├── gui.py              # Tkinter-based GUI logic
├── inventory.py        # Product & Inventory management classes
├── user.py             # User and UserManager classes
├── auth.py             # Authentication logic
├── reports.py          # Reporting utility (low stock, sales summary)
├── utils.py            # Data validation functions
├── .gitignore
├── Report.pdf
└── README.md
```

---

## Requirements

- Python 3.7 or above
- Tkinter (usually comes bundled with Python)

---

## Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [github link]
   cd Inventory-Management-System
   ```

2. **(Optional) Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install any dependencies:**
   - No external dependencies required. Tkinter is included with standard Python distributions.

4. **Run the application:**
   ```bash
   python main.py
   ```

---

## How to Use

### 1. Login

- Enter the username and password to access the system.
- Default credentials:  
  - **Username:** `admin`  
  - **Password:** `admin123`

### 2. Main Menu

- **Add Product:** Enter new product details.
- **View Product Inventory:** See all products. Edit or delete products using the buttons.
- **Low Stock Report:** View products with stock below a specific threshold.
- **Sales Summary Report:** View inventory summary with calculated total values.

### 3. Product Management

- **Add/Edit:** Data is validated for completeness and correctness before saving.
- **Delete:** Remove products with confirmation.

### 4. Reports

- **Low Stock:** Lists products with quantity less than or equal to a user-specified value.
- **Sales Summary:** Shows product-wise and total inventory value.

---

## File Descriptions

- **main.py**  
  Starts the application and launches the GUI.

- **gui.py**  
  Handles all Tkinter GUI screens and user interactions.

- **inventory.py**  
  Contains `Product` and `Inventory` classes for product management and operations.

- **user.py**  
  Defines `User` and `UserManager` classes for authentication.

- **auth.py**  
  Manages user login and authentication logic.

- **reports.py**  
  Provides functions to generate formatted reports (low stock, sales summary).

- **utils.py**  
  Implements data validation functions for product input.

---

## Data Validation

The application enforces strict data validation using the `validate_product_data` function:

- **Product ID & Name:** Must not be empty.
- **Quantity:** Must be a non-negative integer.
- **Price:** Must be a non-negative number.

This ensures that only correct and sensible data is allowed into the system, maintaining inventory integrity.

---

## Extending the Project

- Add persistent storage (e.g., CSV, SQLite) for saving inventory data.
- Implement user roles (admin, staff) for granular access control.
- Add search and filter options for products.
- Integrate export options (CSV/PDF) for reports.
- Enhance UI/UX with additional styling.

---

## Acknowledgements

- [Python](https://www.python.org/)
- [Tkinter Documentation](https://docs.python.org/3/library/tkinter.html)
