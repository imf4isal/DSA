import os
from audioop import reverse

os.system("cls")

# 1.area of circle

# PI = 3.1416

# def area_of_circle(radius):
#     print(PI * radius * radius)

# area_of_circle(3)

# 3. Area Of Rectangle

# def area_of_rectangle(length, width):
#     print(length * width)

# area_of_rectangle(2, 3)

# 22. [Subtract the Product and Sum of Digits of an Integer] (leetcode)
# def subtractProductAndSum(self, n: int) -> int:
#     num = str(n)
#     product_of_digits = 1
#     sum_of_digits = 0
#     for digit in num:
#         digit = int(digit)
#         product_of_digits *= digit
#         sum_of_digits += digit

#     return product_of_digits - sum_of_digits

#23. Input a number and print all the factors of that number

# def factor(number: int):
#     for i in range(1, number + 1):
#         if number % i == 0:
#             print(i)

# factor(10)

#24. Take integer inputs till the user enters 0 and print the sum of all numbers

# run = True
# sum_of_nums = 0

# while (run == True):
#     num = int(input("Put a number: "))

#     if (num == 0):
#         run = False
#     sum_of_nums += num

# print(f"sum of your given numbers is {sum_of_nums}")

# 25. Take integer inputs till the user enters 0 and print the largest number from

# run = True
# numbers = []

# while (run == True):
#     num = int(input("Put a number: "))

#     if (num == 0):
#         run = False
#     numbers.append(num)

# largest_num = max(numbers)
# print(f"Largest number of your given numbers is {largest_num}")

################
############
#####
##########
#intermediate problem

##
##############################################

#17. Reverse A String

# def reverse_string(str):
#     # print(str[::-1])

#     length = len(str)
#     rever = ''
#     # for i in reversed(range(0, length)):
#     #     rever += str[i]

#     for i in range(length - 1, -1, -1):
#         rever += str[i]

#     print(rever)

# reverse_string("faisal")
# # print numbers from 1 to 10 in reverse order
#     for i in range(1, 11)[::-1]:
#         print(i)
