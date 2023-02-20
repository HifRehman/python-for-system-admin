import os
ter_wid=os.get_terminal_size().columns
given_str = input("Enter your string: ")
# print(given_str.center(122))
# print(given_str.ljust(122))
# print(given_str.rjust(122))

print(given_str.center(ter_wid).title())
print(given_str.ljust(ter_wid))
print(given_str.rjust(ter_wid))



