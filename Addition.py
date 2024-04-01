try:
    x = input("Give me the first number to add: ")
    x = int(x)

    y = input("Now give me the second number: ")
    y = int(y)

except ValueError:
    print("Be sure to write a number!")

else:
    sum = x + y
    print(str(x) + "+" + str(y) + "=" + str(sum))