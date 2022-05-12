import os
from re import A

os.system("cls")

#1. [Define two methods to print the maximum and the minimum number respectively among three numbers entered by the user.]

# first = input("Enter first number: ")
# second = input("Enter second number: ")
# third = input("Enter third number: ")

# def max(first, second, third):
#     if (first > second and first > third):
#         return first
#     elif (second > first and second > third):
#         return second
#     else:
#         return third

# print(f"The max number of your given numbers is {max(first, second, third)}")

#2. [Define a program to find out whether a given number is even or odd.]

# num = int(input("Put a number: "))

# def evenorodd(num):
#     if (num % 2 == 0):
#         print("Your given number is even.")
#     else:
#         print("Your given number is odd.")

# evenorodd(num)

#3. [A person is eligible to vote if his/her age is greater than or equal to 18. Define a method to find out if he/she is eligible to vote.]

# age = int(input("Can you vote? Let's check. \nWhat is your age? "))

# def isEligibleforVote(age):
#     if age >= 18:
#         print("You are eligible as a voter.")
#     else:
#         print("You are not eligible as a voter.")

# isEligibleforVote(age)

#4. [Write a program to print the sum of two numbers entered by user by defining your own method.]

# num1 = int(input("enter first number: "))
# num2 = int(input("enter second number: "))

# def sum(num1, num2):
#     return num1 + num2

# print(f"The sum of your two number is {sum(num1, num2)}")

# product of two numbers

# def product(num1, num2):

#     product1 = []
#     product2 = []
#     commonproduct = []
#     for i in range(1, num1 + 1):
#         if (num1 % i == 0):
#             product1.append(i)
#     for i in range(1, num2 + 1):
#         if (num2 % i == 0):
#             product2.append(i)

#     for pro1 in product1:
#         for pro2 in product2:
#             if (pro1 == pro2):
#                 commonproduct.append(pro1)

#     print(f"Product of {num1} is {tuple(product1)}")
#     print(f"Product of {num2} is {tuple(product2)}")
#     print(f"Common Product of {num1} and {num2} is {tuple(commonproduct)}")

# product(num1, num2)

#is prime or not

# number = int(input("Enter a number to check if it's prime or not: "))

# def isPrime(num):

#     prime = True
#     for i in range(2, number):
#         if (number % i == 0):
#             prime = False
#         else:
#             i = i + 1

#     if (prime == True):
#         print(f"Your given number {num} is prime.")
#     else:
#         print(f"Your given number {num} is not a prime.")

# isPrime(number)

# factorial of a given number

# number = int(input("Give a number to get it's factorial: "))

# def factorial(number):
#     factorial = 1
#     if (number > 0):
#         for i in range(1, number + 1):
#             factorial *= i

#     print(f"The factorial of your given number {number}! is {factorial}.")

# factorial(number)

# #is palindrome

# number = int(input("enter a number to check if it's palindrome: "))

# def ispalindrome(number):
#     num = str(number)

#     print(num)
#     ispalindromenum = False
#     for i in range(0, len(num)):
#         print(num[i])
#         if (num[i] == num[-i - 1]):
#             ispalindromenum = True
#     print(ispalindromenum)

# ispalindrome(number)

#12. [Write a function to check if a given triplet is a Pythagorean triplet or not.]

# print("check if a given triplet is a Pythagorean triplet or not.")
# a = int(input("a: "))
# b = int(input("b: "))
# c = int(input("c: "))

# aa = a * a
# bb = b * b
# cc = c * c

# if (aa + bb == cc or bb + cc == aa or aa + cc == bb):
#     print("This triplet is Pythagorean.")
# else:
#     print("This triplet is not Pythagorean.")

#13. [Write a function that returns all prime numbers between two given numbers.]

# print(
#     "Check all prime numbers between two given numbers(including given numbers). Enter your two numbers."
# )
# number1 = int(input("Start: "))
# number2 = int(input("End: "))

# def primeBetweenTwo(number1, number2):
#     primes = []

#     for r in range(number1, number2 + 1):
#         rPrime = True
#         for i in range(2, r):
#             if (r % i == 0):
#                 rPrime = False
#         if (rPrime == True):
#             primes.append(r)

#     print(
#         f"prime numbers between {number1} and {number2} : {tuple(primes)}. \n Total: {len(primes)}"
#     )

# primeBetweenTwo(number1, number2)

#sum of the first n natural number

n = int(input("Get the sum of the first n natural numbers.\nN: "))


def sumoffirstN(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i

    return sum


print(sumoffirstN(n))
