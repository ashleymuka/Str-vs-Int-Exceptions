'''
Description: write a program to read a list of names and ages, and the program should output that list with the age incremented by one
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
