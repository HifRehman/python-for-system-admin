# import os
# t_w = os.get_terminal_size().columns

# given_str = input("Enter you string: ")
# print(given_str.center(t_w).title())
# print(given_str.ljust(t_w).title())
# print(given_str.rjust(t_w).title())

# my_even_no = [0,2,4,6,8,10]
# usr_num = eval(input('Enter your number: '))
# if usr_num in my_even_no:
#     print("your given num is even num.")
# else:
#     print("not an even num")


# num1 = eval(input("Enter your first num: "))
# num2 = eval(input("Enter your second num: "))

# if num1 == num2:
#     print(f"Number {num1} is equal to {num2}.")
# elif num1 > num2:
#     print(f"Number {num1} is bigger")
# else:
#     print(f"Number {num2} is bigger")


# Conver number into word.

num = eval(input("Enter your number between 1-10 range: "))
num_word = {1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine", 10:"ten"}

if num in [1,2,3,4,5,6,7,8,9,10]:
    print(num_word.get(num))
else:
    print("Number is out of range")

