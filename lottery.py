from random import choice
lottery_int = [1, 12, 23, 7, 37, 9, 42, 8, 11, 87]
lottery_letter = ['m', 'a', 'r', 'q', 'l']
winners = ""
chosen = 0
while chosen <= 3:
    selection = choice(lottery_int)
    winners += f"{selection} "
    chosen += 1

message = input("Enter your lottery numbers here (4 numbers, 1 letter): ")
print(message)

print(f"The lottery numbers are: {winners} {choice(lottery_letter)}")

if message == f"{winners}{choice(lottery_letter)}":   
    print("You win!")
else:
    print("Better luck next time!")