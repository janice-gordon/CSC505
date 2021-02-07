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
# inspiration was provided by the following articles:
# https://www.geeksforgeeks.org/python-program-to-create-bankaccount-class-with-deposit-withdraw-function/
# https://www.engineeringbigdata.com/python-atm-code-for-account-balance-withdraw-and-deposit-functions/#Create_Class_and_Define_Functions

"""
import pandas as pd
from sys import exit

#import fake account data from csv
accounts_df = pd.read_csv('accounts.csv', sep=',', dtype={'aid':str,'name':str,'pin':str,'balance':float})

# function to convert float to currency format for printing
def getCurrency(amount):
    currency = "${:,.2f}".format(amount)
    return currency

def getWelcome(random_account):
    act = random_account
    customer_name = act.getName()
    print("\nWelcome " + customer_name + "!")

def getHelp():
    help = "Please contact customer service for assistance."
    return help

# sample a random account for demonstration purposes
def getRandomAccount():
    sample_row = accounts_df.sample(n=1,replace=True)
    name = sample_row.iloc[0]['name']
    pin = sample_row.iloc[0]['pin']
    balance = sample_row.iloc[0]['balance']
    random_account = Account(name,pin,balance)
    return random_account
  
def checkPIN(the_pin,pin_attempt):
    if pin_attempt == the_pin:
        return True
    else:
        return False

def login(the_pin,pin_attempt):
    # User gets 5 password attempts before account locks
    attempts = 1
    while attempts <= 4:
        if checkPIN(the_pin,pin_attempt): 
            return True
            break
        else:
            print("Incorrect PIN, please try again: ")
            pin_attempt = input()
            attempts += 1
    support_msg = getHelp()
    print("You have entered too many incorrect PIN numbers, your account is now locked. " + support_msg)
    exit()
    
def accountActions(random_account):
    act = random_account
    current_balance = act.getBalance()
    customer_name = act.getName()
        
    if current_balance <= 0:
        support_msg = getHelp()
        print("Your account balance is now insufficient, the account will be closed. " + support_msg)
        exit()

    else:
        print("Choose an option (enter a number): ")
        selection = int(input("1 - View Balance \t 2 - Withdraw \t 3 - Deposit \t 4 - Exit\n"))
        
        if selection == 1:
            balance = act.getBalance()
            print("You have " + getCurrency(balance) + " in your account.\n")
            accountActions(random_account)
        
        elif selection == 2:
            amt = float(input("Enter amount to withdraw: "))
            if amt > act.getBalance():
                print("Sorry you don't enough money in your account to withdraw " + getCurrency(amt))
            else:
                withdrawal = act.withdraw(amt)
                new_balance = act.getBalance()
                print("Your new account balance is: " + getCurrency(new_balance))
            accountActions(random_account)
            
        elif selection ==3:
            amt = float(input("Enter amount to deposit: "))
            deposit = act.deposit(amt)
            new_balance = act.getBalance()
            print("Your new account balance is: " + getCurrency(new_balance))
            accountActions(random_account)
            
        elif selection == 4:
            print("Have a great day " + customer_name + "! Goodbye.")
            exit()
    
class Account:
    def __init__(self, name, pin, balance=0): 
        self.pin = pin
        self.balance = balance
        self.name = name
       
    def getName(self):
        return self.name
    
    def getPin(self):
        return self.pin
    
    def getBalance(self):
        return self.balance
    
    def withdraw(self, amount):
        self.balance -= amount
        
    def deposit(self, amount):
        self.balance += amount


def main():
    #instantiate a random account for demonstration purposes
    random_account = getRandomAccount()
    the_pin = random_account.getPin()
    balance = random_account.getBalance()
    
    print("Please enter your PIN. (hint: " + the_pin + "):")
    pin_attempt = input()
    login(the_pin,pin_attempt)
    
    if login:
        getWelcome(random_account)
        accountActions(random_account)
        
    
if __name__ == "__main__":
    main()   
