"""
Take Input From User and Pass It To Function to Calculate Square
#Author : Sandeep Patil
"""

def cal_sqr(num):
    return num ** 2

num = int(input('Enter The Num = '))

result = cal_sqr(num)

#.format is used to print the Number and It's Square Off
print('Square Of {} Is {}'.format(num,result))