"""
Calculate the multiplication and sum of two numbers
Given two integer numbers, return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.

"""

def mltplctn (num1,num2):
    return num1 * num2

def sum_num(num1,num2):
    return num1 + num2


num1 = int(input("Enter Num1 = "))
num2 = int(input('Enter Num2 = '))

if (num1 * num2 <= 1000):
    result= mltplctn(num1,num2)
else:
    result = sum_num(num1,num2)

print(f'Result = {result}')