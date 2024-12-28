import sys
import os

# Add the current directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from bank_account import BankAccount  # Import BankAccount class

# Your test cases go here...


import pytest
from bank_account import BankAccount

# Test Deposit
def test_deposit_valid():
    account = BankAccount('Alice', 100)
    new_balance = account.deposit(50)
    assert new_balance == 150

def test_deposit_invalid():
    account = BankAccount('Alice', 100)
    with pytest.raises(ValueError, match="Deposit amount must be positive"):
        account.deposit(-50)

# Test Withdraw
def test_withdraw_valid():
    account = BankAccount('Bob', 200)
    new_balance = account.withdraw(50)
    assert new_balance == 150

def test_withdraw_invalid_amount():
    account = BankAccount('Bob', 200)
    with pytest.raises(ValueError, match="Withdrawal amount must be positive"):
        account.withdraw(-50)

def test_withdraw_insufficient_funds():
    account = BankAccount('Bob', 200)
    with pytest.raises(ValueError, match="Insufficient funds"):
        account.withdraw(250)

# Test Transfer
def test_transfer_valid():
    account1 = BankAccount('Alice', 500)
    account2 = BankAccount('Bob', 300)
    new_balance1, new_balance2 = account1.transfer(account2, 200)
    assert new_balance1 == 300
    assert new_balance2 == 500

def test_transfer_invalid_amount():
    account1 = BankAccount('Alice', 500)
    account2 = BankAccount('Bob', 300)
    with pytest.raises(ValueError, match="Transfer amount must be positive"):
        account1.transfer(account2, -100)

def test_transfer_insufficient_funds():
    account1 = BankAccount('Alice', 100)
    account2 = BankAccount('Bob', 300)
    with pytest.raises(ValueError, match="Insufficient funds for transfer"):
        account1.transfer(account2, 200)

# Test Account Details
def test_account_str():
    account = BankAccount('Charlie', 1000)
    assert str(account) == "BankAccount(owner: Charlie, balance: 1000)"
