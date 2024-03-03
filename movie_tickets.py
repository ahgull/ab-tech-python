age = input("What is the age of the ticket holder? ")
age = int(age)
total_price = 0
if age < 3:
    total_price += 0
elif age < 12:
    total_price += 10
elif age > 12:
    total_price += 15
print(f"\nYour total price is ${total_price}.")
active = True
while active:
    message = input("Want more? (Yes/No) ")
    if message == "No":
        active = False
    else:
        age = age = input("What is the age of the ticket holder? ")
        age = int(age)
        print(f"\nYour total price is ${total_price}.")