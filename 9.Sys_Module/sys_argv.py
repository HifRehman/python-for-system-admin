import sys

'''
sys.argv returns a list of command line arguments passed to a Python script.
sys.argv giving a list.
'''

print(sys.argv)

# [ansadmin@cd-devops-3 py-for-sys]$ /usr/local/bin/python3.8 /home/ansadmin/py-for-sys/Sys_Module/sys_argv.py hi kells wow 12
# ['/home/ansadmin/py-for-sys/Sys_Module/sys_argv.py', 'hi', 'kells', 'wow', '12']
# [ansadmin@cd-devops-3 py-for-sys]$ 

print(sys.argv[0])

# [ansadmin@cd-devops-3 py-for-sys]$ /usr/local/bin/python3.8 /home/ansadmin/py-for-sys/Sys_Module/sys_argv.py hi 12
# ['/home/ansadmin/py-for-sys/Sys_Module/sys_argv.py', 'hi', '12']
# /home/ansadmin/py-for-sys/Sys_Module/sys_argv.py
# [ansadmin@cd-devops-3 py-for-sys]$ 

# usr_str = input("Enter your string: ")
# usr_action = input("Enter your action (valid: lower/upper/title)")

# print("The no of command line argument", len(sys.argv))
if len(sys.argv) != 3:
    print("Usage:")
    print(f"{sys.argv[0]} <your string> <your action>")
    sys.exit()

usr_str = sys.argv[1]
usr_action = sys.argv[2]

if usr_action == 'lower':
    print(usr_str.lower())
elif usr_action == 'upper':
    print(usr_str.upper())
elif usr_action == 'title':
    print(usr_str.title())
else:
    print("your option is invalid")

# [ansadmin@cd-devops-3 py-for-sys]$ /usr/local/bin/python3.8 /home/ansadmin/py-for-sys/Sys_Module/sys_argv.py 'kells kells' upper
# ['/home/ansadmin/py-for-sys/Sys_Module/sys_argv.py', 'kells kells', 'upper']
# /home/ansadmin/py-for-sys/Sys_Module/sys_argv.py
# KELLS KELLS
# [ansadmin@cd-devops-3 py-for-sys]$ 


