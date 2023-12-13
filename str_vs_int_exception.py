'''
Author: Ashley Muka
Assignment Title:String vs int exceptions
Assignment Description: write a program to read a list of names and ages
and the program fails is the wrong type is input
Due Date:09/08/2023
date Created:09/08/2023
Date Last Modified:09/08/2023

'''

parts = input().split()
name = parts[0]

while name != '-1':
    try:
        age = int(parts[1]) + 1
        
    except ValueError:
        age = 0
    
    print(f'{name} {age}')

    parts = input().split()
    name = parts[0]
