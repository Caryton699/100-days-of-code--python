a= int(input("Enter a number: "))
for i in range(12):
    if i == 11:
        break
    print(a ,"x" ,i ,"=" , i*a)
print("I'm Out of the loop")