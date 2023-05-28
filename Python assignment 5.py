#!/usr/bin/env python
# coding: utf-8

# ## Python Basic Programming Assignment - 5
# --------------
# 

# ### 1. Write a Python Program to Find LCM?

# In[1]:


def find_lcm(num1, num2):
    # To Find the maximum of the two numbers
    max_num = max(num1, num2)
    lcm = max_num

    while True:
        if lcm % num1 == 0 and lcm % num2 == 0:
            # If the LCM is divisible by both numbers, exit the loop
            break
        lcm += max_num

    return lcm

# Example usage
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

result = find_lcm(number1, number2)
print(f"The LCM of {number1} and {number2} is: {result}")


# ### 2. Write a Python Program to Find HCF?

# In[2]:


def find_hcf(num1, num2):
    # Find the minimum of the two numbers
    min_num = min(num1, num2)

    hcf = 1  # Initialize HCF as 1

    for i in range(1, min_num + 1):
        if num1 % i == 0 and num2 % i == 0:
            hcf = i

    return hcf

# Example usage
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

result = find_hcf(number1, number2)
print(f"The HCF of {number1} and {number2} is: {result}")


# ### 3. Write a Python Program to Convert Decimal to Binary, Octal and Hexadecimal?

# In[3]:


def decimal_to_binary(decimal):
    binary = bin(decimal).replace("0b", "")
    return binary

def decimal_to_octal(decimal):
    octal = oct(decimal).replace("0o", "")
    return octal

def decimal_to_hexadecimal(decimal):
    hexadecimal = hex(decimal).replace("0x", "")
    return hexadecimal

# Example usage
decimal_number = int(input("Enter a decimal number: "))

binary_result = decimal_to_binary(decimal_number)
octal_result = decimal_to_octal(decimal_number)
hexadecimal_result = decimal_to_hexadecimal(decimal_number)

print(f"Binary representation: {binary_result}")
print(f"Octal representation: {octal_result}")
print(f"Hexadecimal representation: {hexadecimal_result}")


# ### 4. Write a Python Program To Find ASCII value of a character?

# In[4]:


character = input("Enter a character: ")

# Get the ASCII value using the ord() function
ascii_value = ord(character)

print(f"The ASCII value of {character} is: {ascii_value}")


# ### 5. Write a Python Program to Make a Simple Calculator with 4 basic mathematical operations?

# In[6]:


def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Error: Division by zero"

print("Simple Calculator")
print("Operations: ")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

operation = int(input("Select an operation (1-4): "))

number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

if operation == 1:
    result = add(number1, number2)
    operation_symbol = "+"
elif operation == 2:
    result = subtract(number1, number2)
    operation_symbol = "-"
elif operation == 3:
    result = multiply(number1, number2)
    operation_symbol = "*"
elif operation == 4:
    result = divide(number1, number2)
    operation_symbol = "/"
else:
    print("Invalid operation selected")
    exit()

print(f"\n{number1} {operation_symbol} {number2} = {result}")


# In[ ]:




