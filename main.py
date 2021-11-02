import math
import random 




# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# num3 = int(input("Enter third number: "))
# sum = num1 + num2 + num3
# avg = sum / 3
# print("The sum is", sum)
# print("The average is", avg)


# # or round avg to 2 decimal places using the print formatting option with decimal modifiers.
# print(f"The average is {avg:.2f}")

# Math functions, random, and pi 
# Using // for integer division 
# print(7/4)  # 1.75
# print(7//4)  # 1 
# print(11 // 3) # 3

# math.pi
print(math.pi)
# circumference of a circle with radius 4
print(2 * math.pi * 4)
r = 4
print(2 * math.pi * r)

# math.sqrt() - square root 
print(math.sqrt(25))  # 5.0
print(math.sqrt(27))  # 5.196....

# math.pow() - raise a number to a power 
print(math.pow(3, 2))  # base = 3, exponent = 2
print(math.pow(2, 3))  # 8.0

print(math.pow(2, 3) * (math.sqrt(25))) # 8 x 5

# math.floor() - rounding the number down to the lower integer
print(math.floor(3.14))   # 3
print(math.floor(3.999))  # 3

# math.ceil() - rounding the number up to the next integer

print(math.ceil(4.123)) # 5
print(math.ceil(4.99999))  # 5

# round() - rounds a number
print(round(3.14)) # 3
print(round(3.5))  # 4, 
a = 3.141592653
print(round(a, 3)) # to 3 decimal places
print(round(a, 4)) # to 4 decimal places

# Using random() to generate random numbers
# random.randint(start, end) - generates random integer numbers
print(random.randint(1, 10)) # random numbers 1 to 10

# random.uniform() - generates random decimal numbers
print(random.uniform(1, 10))

# random.choice()
names = ["Joe", "Bob", "Tom", "Jim"]
print(random.choice(names))









