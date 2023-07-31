![GitHub Repo stars](https://img.shields.io/github/stars/awaisyasin/qbank-app?style=social)
![GitHub forks](https://img.shields.io/github/forks/awaisyasin/qbank-app?style=social)
![GitHub watchers](https://img.shields.io/github/watchers/awaisyasin/qbank-app?style=social)
![Downloads](https://img.shields.io/pypi/dm/project-name.svg)
[![Issues](https://img.shields.io/github/issues/awaisyasin/qbank-app.svg)](https://github.com/awaisyasin/qbank-app/issues)
[![Pull Requests](https://img.shields.io/github/issues-pr/awaisyasin/qbank-app.svg)](https://github.com/awaisyasin/qbank-app/pulls)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/badge/version-1.0-green.svg)](https://github.com/awaisyasin/qbank-app/releases)
# QBank App

This is a Python script that implements a simple banking application with a graphical user interface (GUI) using the PyQt5 library. The script allows the user to deposit or withdraw money and displays the current balance along with the last deposited and withdrawn amounts.

## Dependencies

- Python 3.x
- PyQt5

## Usage

To run the script, open a terminal or command prompt and navigate to the directory containing the script file. Then type the following command or simply download the app form [here](https://github.com/awaisyasin/qbank-app/tree/main/app):

```
python QBank.py
```

This will launch the QBank application window.

## Features

- Deposit money to the account
- Withdraw money from the account
- Display current balance
- Display last deposited amount
- Display last withdrawn amount

## How it Works

The script defines a `Bank` class that keeps track of the available balance, last deposited amount, and last withdrawn amount. The `Bank` class also defines methods for depositing and withdrawing money from the account, and for displaying the current balance and transaction history.

The GUI is implemented using PyQt5. It consists of a main window with a dropdown menu for selecting an option, a text box for entering an amount, a submit button, and an LCD display for displaying the balance or transaction history.

When the user selects an option from the dropdown menu and enters an amount, the script calls the appropriate method of the `Bank` class to perform the transaction. The script then updates the LCD display with the new balance or transaction history.

If the user selects "Last Deposit Amount", "Last Withdraw Amount", or "Current Amount" from the dropdown menu, the text box is disabled and the script displays the corresponding value in the LCD display.
