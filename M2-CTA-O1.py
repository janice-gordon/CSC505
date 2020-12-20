#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###########################################################
# CSC505 Module 2 - Option 1
# Python Script - Capture & Print Stakeholder Requirement
# Janice Gordon
###########################################################

print("Type your requirements, hit enter after each (type q to quit): ")

reqs = []

while True:
    userInput = input()
    if str.lower(userInput) == "q":
        break
    reqs.append(userInput)
    
print("\n=================================")
print("Your requirements are: \n")
for iteration, requirements in enumerate(reqs):
    print(str(iteration + 1) + ". " + requirements + "\n")
print("=================================")

