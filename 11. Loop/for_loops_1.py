my_list = [2,3,4,5]
for i in my_list:
    print(i)

'''
Python has 2 types of loops.
- for loop
- while loop

for loop: for loop in python is used to iterate over a sequence (list, tuple, string) or other iterable objects.



'''

for value in (4,5,6,7,"Hi"):
    print("======")
    print(value)

for each_char in "python":
    print("- - - - - - - -", each_char)

for each in my_list:
    rem=each%2
    if rem==0:
        print(f"{each} is even")
    else:
        print(f"{each} is odd")
