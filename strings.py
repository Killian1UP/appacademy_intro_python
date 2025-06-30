# Advanced concepts - Strings

message = " Hello, World! "

# Indexing
print(message[0])
print(message[1])
print(message[-1])

# length of string
print(len(message))

print(message.strip()) # removing leading and trailing whitespaces 
print(message.lower()) # converts all characters to lowercase
print(message.split(',')) # split the string into a list based on the comma
print(message.upper()) # converts all characters to uppercase
print(message.replace('Hello', 'No')) # replace a character or string with a different value 

# Control statements 
# Part 1

num = 0

if num > 0:
   print("The number is positive")
elif num == 0:
   print("The number is zero")
else:
   print("The number is negative")
    
# Part 2
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num1 > num2:
   print(num1, "is greater than" ,num2)
elif num1 < num2:
   print(num2, "is greater than" ,num1)
else:
   print("Both numbers are equal")

# Loops
# For Loop

fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
   print(fruit)
    
numbers = [1, 2, 3, 5, 7]

for number in numbers:
   print(number)

# While loops
# Using a while loop to count from 1 to 5

count = 1

while count <=5:
    print(count)
    count += 1  #Increment the count by 1

# Operators on strings

str1 = "I am hungry"
str2 = "I need McDonald's"

print(str1 + ", " + str2)

word = "Fein"
print(word * 4)