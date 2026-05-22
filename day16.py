a = int(input("Enter your age: "))
print("Your age is:", a)
match a:
    case a if a < 18:
        print("You are not eligible to vote.") #the space before print function is called indentation.
    case a if a >= 18:
        print("Congratulations! You are eligible to vote.")
    case _:
        print("You are eligible to vote.")
    