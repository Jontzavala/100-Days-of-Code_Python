print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
adult_ticket_cost = 12
teen_ticket_cost = 7
young_kid_ticket_cost = 5
photo_cost = 3

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    ticket_cost = 0
    if age <= 12:
        ticket_cost = young_kid_ticket_cost
    elif age <= 18:
        ticket_cost = teen_ticket_cost
    else:
        ticket_cost = adult_ticket_cost
    photo = input("Do you want a photo? ")
    if photo == "yes":
        print(f"That will be an extra ${photo_cost}. That brings you total to ${photo_cost + ticket_cost}")
    else:
        print(f"Your total is ${ticket_cost}")
else:
    print("Sorry you have to grow taller before you can ride.")
