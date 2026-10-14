# ATM Simulation in Python

This is a simple command-line ATM simulation program written in Python.  
It allows a user to:

- Check balance  
- Deposit money  
- Withdraw money  
- Exit the system  

The project is made for learning basic Python concepts such as functions, loops, conditionals, and user input.

---

## Features

- **Welcome screen** showing a greeting message.
- **Fixed starting balance** (default: 1000).
- **Menu-based system** using a `while True` loop.
- Option to:
  - Check current balance
  - Deposit an amount
  - Withdraw an amount (with insufficient balance check)
  - Exit the program safely

---

## How It Works

- The program starts by calling the `atm_simulation()` function.
- A variable `balance` is initialized with a default value of `1000`.
- Inside a `while True` loop, a menu is displayed to the user:
  1. Check balance  
  2. Deposit money  
  3. Withdraw money  
  4. Exit  
- Based on the user’s choice (`input()`), an `if-elif` block runs the corresponding operation.
- The loop continues until the user selects option **4 (Exit)**.

---

## Technologies Used

- **Language:** Python  
- **Concepts:**  
  - Functions  
  - Variables  
  - While loop  
  - If-elif-else conditions  
  - User input handling

---

## How to Run

1. Make sure you have **Python 3** installed on your system.
2. Download or clone this repository:

   ```bash
   git clone https://github.com/YOUR-USERNAME/python-atm-simulation.git
   cd python-atm-simulation
