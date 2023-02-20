'''
Exceptions can handled by using try and except statement.

Errors 2 Types :- 
1. Syntax Error --> No way to handle syntax errors.
2. Runtime error  --> Exceptions, way to handle runtime errors/exception

Exceptions Examples:

- IndexError
- ZeroDivisionError
- ImportError
- ValueError
- NameError
- FileNotFoundError
'''

# print("Welcome to the TechwitHif")
# try:
#     print(4/0)
# except:
#     print("Zero Division Error")

# try:
#     fo=open("kells.txt")
#     print(fo.read())
#     fo.close()
# except Exception as e:
#     print(e)

# my_list = [3,4,5]
# try:
#     print(my_list(4))
# except Exception as e:
#     print(e)

try:
    import fabric
except Exception as e:
    print(e)