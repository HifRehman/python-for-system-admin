import getpass

'''
getpass() :- prompt the user for a password without echoing. The getpass module provides a secure way to handle the 
password prompts where programs interacts with the users via the terminal

getuser() :- function displays the login name of the user. This function checks the environment variables 
LOGNAME, USER, LNAME and USERNAME, in order, and returns the value of the first non-empty string.

'''

# print(dir(getpass))

# db_pass = input("Enter your password : ") -> for password wrong way

# db_pass = getpass.getpass("ENter your password")
# print(db_pass)

print(getpass.getuser())

