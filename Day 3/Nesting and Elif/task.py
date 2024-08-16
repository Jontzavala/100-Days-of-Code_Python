print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
age = int(input("How old are you?"))

if height >= 120:
    if age > 18:
        print("You can ride the rollercoaster and since you're over 18 your ticket cost $12.")
    elif age >= 12 and age <= 18:
        print("You can ride the rollercoaster and since you're between 12 and 18 your ticket cost $7.")
    else:
        print("You can ride the rollercoaster and since you're younger than 12 your ticket is only $5!")

else:
    print("Sorry you have to grow taller before you can ride.")
