import os

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

num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))

# def sum(num1, num2):
#     return num1 + num2

# print(f"The sum of your two number is {sum(num1, num2)}")

# product of two numbers


def product(num1, num2):

    product1 = []
    product2 = []
    commonproduct = []
    for i in range(1, num1 + 1):
        if (num1 % i == 0):
            product1.append(i)
    for i in range(1, num2 + 1):
        if (num2 % i == 0):
            product2.append(i)

    for pro1 in product1:
        for pro2 in product2:
            if (pro1 == pro2):
                commonproduct.append(pro1)

    print(f"Product of {num1} is {tuple(product1)}")
    print(f"Product of {num2} is {tuple(product2)}")
    print(f"Common Product of {num1} and {num2} is {tuple(commonproduct)}")


product(num1, num2)
