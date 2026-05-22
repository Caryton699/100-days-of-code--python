a = int(input("Enter your age: "))
print("Your age is:", a)

#conditional operations
# >, <, >=, <=, ==, !=

if a < 18:
    print("You are not eligible to vote.") #the space before print function is called indentation.

elif a >= 18:
    print("Congratulations! You are eligible to vote.")
else:
    print("You are eligible to vote.")