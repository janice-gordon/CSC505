#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 13:37:54 2021
@author: janicegordon
requirments:
•	The customer must pass authentication before withdrawing money.
•	Authentication is performed by checking a PIN.
•	The PIN can be correct or not.
•	Unsuccessful attempts are counted.
•	If the counter exceeds a limit, then the customer is rejected.
•	If the account balance is zero, then the account is closed.	

# Class for Account - Balance, PIN, etc.
# Function to check PIN
# Function to check account balance
# https://www.geeksforgeeks.org/python-program-to-create-bankaccount-class-with-deposit-withdraw-function/
# https://www.engineeringbigdata.com/python-atm-code-for-account-balance-withdraw-and-deposit-functions/#Create_Class_and_Define_Functions

## Todo List
# Figure out zero balance
# Figure out checking balance prior to withdraw
# Clean up how $ amounts are displayed

"""
import pandas as pd
from sys import exit

#import fake account data from csv
accounts_df = pd.read_csv('accounts.csv', sep=',', dtype={'aid':str,'pin':str,'balance':float})


#pull up random account information for demonstration purposes
def getRandomAccount():
    sample_row = accounts_df.sample(n=1,replace=True)
    pin = sample_row.iloc[0]['pin']
    balance = sample_row.iloc[0]['balance']
    random_account = Account(pin, balance)
    return random_account
  
def checkPIN(the_pin,pin_attempt):
    print("The correct pin is:",the_pin)
    print("You entered:", pin_attempt)
    if pin_attempt == the_pin:
        return True
    else:
        return False

def login(the_pin,pin_attempt):
    # User gets 5 password attempts before account locks
    attempts = 1
    while attempts <= 4:
        if checkPIN(the_pin,pin_attempt): # function returns True
            #print("That is correct, what would you like to do next?")
            return True
            break
        else:
            print("Incorrect PIN, please try again: ")
            pin_attempt = input()
            attempts += 1
    print("You have entered too many incorrect PIN numbers, your account is now locked. Please call customer service for assistance.")
    exit()
    
def accountActions(random_account):
    act = random_account
    current_balance = act.getBalance()
    print("\nWelcome Bank Customer!")
    print("Your current balance is: " + str(current_balance))
    print("What would you like to do today?")
    selection = int(input("1 - View Balance \t 2 - Withdraw \t 3 - Deposit \t 4 - Exit\n"))
    
    if selection == 1:
       # get balance
        balance = act.getBalance()
        print(balance)
    
    elif selection == 2:
        amt = float(input("Enter amount to withdraw: "))
        withdrawal = act.withdraw(amt)
        new_balance = act.getBalance()
        print(new_balance)
        
    elif selection ==3:
        amt = float(input("Enter amount to deposit: "))
        deposit = act.deposit(amt)
        new_balance = act.getBalance()
        print(new_balance)
        
    elif selection == 4:
        print("Goodbye")
        exit()
    
class Account:
    def __init__(self, pin, balance=0): 
        self.pin = pin
        self.balance = balance
       
    def getPin(self):
        return self.pin
    
    def getBalance(self):
        return self.balance
    
    def withdraw(self, amount):
        self.balance -= amount
        
    def deposit(self, amount):
        self.balance += amount



def main():
    #instantiate a random account
    random_account = getRandomAccount()
    the_pin = random_account.getPin()
    balance = random_account.getBalance()
    
    print("Please enter your PIN. (hint: " + the_pin + "):")
    pin_attempt = input()
    login(the_pin,pin_attempt)
    
    if login:
        accountActions(random_account)
    
        
     

if __name__ == "__main__":
    main()   
