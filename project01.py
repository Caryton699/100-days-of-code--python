print("Calculator")
print("supported operations: +, -, *, /")

a = int(input("Enter your first number :"))

b = int(input("Enter your second number :"))

c = input("which operation would you like to do? :")

if c == "+":
    print("The sum of", a, "and", b, "is", a + b)

elif c == "-":
    print("The difference of", a, "and", b, "is", a - b)

elif c == "*":
    print("The product of", a, "and", b, "is", a * b)

elif c == "/":
    if b != 0:
        print("The quotient of", a, "and", b, "is", a / b)
    else:
        print("Error: Division by zero is not allowed.")