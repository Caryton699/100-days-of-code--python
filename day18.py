# # For Loop ---

for i in range(3 , 31 , 3):
    print(i)

# # While Loop ---

i = 0
while(i<31):
    print(i)
    i = i + 3

# While loop example with user input

i = int(input("Enter a number: "))

while i<=38:
    i = int(input("Enter a number: "))
    print("You entered: ", i)
print("Goodbye")

# For loop example with user input

for _ in range(5):
    i = int(input("Enter a number: "))
    print("You entered: ", i)
print("Goodbye")

# note : many times in interview the ask to emulate do while loop in python using while loop or for loop.

i = int(input("Enter a number: "))
while True:
    print("You entered: ", i)
    if i>38:
        break
    i = int(input("Enter a number: "))