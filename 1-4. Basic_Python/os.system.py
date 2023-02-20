# os.system() is used to execute os commands

# os.getcwd() -> for current working directory
# os.listdir() -> listing directory on CWD

import os
# print(os.system("ls"))
# print(os.system("free -m"))
rt = os.system("ls")

cmd="date"
x = os.system(cmd)
if x == 0:
    print("success")
else:
    print("failure")



