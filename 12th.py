fruits = "apple,banana,orange,grape,kiwi"

print(len(fruits))  # Output: 30

print(fruits[0:5])  # Output: apple

print(fruits[6:12])  # Output: banana

print(fruits[13:19])  # Output: orange

print(fruits[20:25])  # Output: grape

print(fruits[26:30])  # Output: kiwi

#Negative slicing: 
print(fruits[0:-25])  # Output: kiwi

#Expanded form
print(fruits[0:len(fruits)-25])  # Output: apple


# Previous video code quiz
alphabet = "abcdefghijklmnopqrstuvwxyz"
for i in alphabet:
    print(i)                                #for writing each character in a new line i.e. in vertical order.


#QUIZ
nm = "harry"
print(nm[-4:-2])  # Output: ar