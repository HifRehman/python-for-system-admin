import os
import time
import platform

def my_code(cmd1,cmd2):
    time.sleep(2)
    os.system(cmd1)
    time.sleep(2)
    os.system(cmd2)
if platform.system()=="Windows":
    my_code("cls", "dir")
else:
    my_code("clear", "ls -lart")

