# First
name = str(input("Your first name:"))
surname = str(input("Your last name"))
age = int(input("Your age:"))
number = input("Your phone number:")

print("Your first name is" ,FirstName," your second name is" ,LastName)
print("Your age is ",age )
print("Yo  ur phone number is  ",number )

# Second

a = int(input("Enter a: "))
b = int(input("Enter b: "))
print("Area of rectangle is" , a*b)
print("Area of square of a is" , a*a)
print("Area of square of b is" , b*b)

# Third

import math
a=float(input("Enter real num which contain 2 digits before and 2 digits after the coma: "))
b=a//1
c=a%1
b1=b/100
c1=c*100
num = c1+b1
print(num)

# Fourth
import math
A = int(input("Enter A"))
Y =math.pow(A,2)/3 + (math.pow(A,2) +4 )/6 + math.sqrt(math.pow(A,2)+4)/4 + math.sqrt(math.pow(math.pow(A,2)+4,3))/4
print("Y is equal to " , Y)

# Fifth
number = int(input("N is"))
print((number*5+8)*2)

# Second page
# 2.1

num1 = int(input("First number:"))
operation = input("Operation:")
num2 = int(input("Second number:"))
if operation == "+":
    print(num1 + num2)
elif operation == "-":
    print(num1-num2)
elif operation == "*":
    print(num1*num2)
else:
    print(num1/num2)

# 2.2

num1 = int(input("First number:"))
operation = input("Operation:")
num2 = int(input("Second number:"))
def calc(num1,operation,num2):
    if operation == "+":
        return (num1 + num2)
    elif operation == "-":
        return (num1-num2)
    elif operation == "*":
        return (num1*num2)
    else:
        return (num1/num2)
print("Can't divide by 0") if(num2 == 0 and operation == "/") else print(calc(num1,operation,num2))

# 2.3

number = 14
if(number>10 and number!=12 and number<=15 or number==18):
    print("True")

# 2.4

start = 34
while (start<66):
    start+=2
    print(start)

# 2.5
boolean = True
boolean2 = False
while True:
    if boolean==boolean2:
        print("First interation")
        break

# 2.6

for number in range(1,101):
    if(number!=50 and number!=99):
        print(number)

# 2.7(Last)
word = str(input("Enter the word "))
number = int(input("Enter the number "))
for letters in word:
    print(letters * number)