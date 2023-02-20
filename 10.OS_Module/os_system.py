import os
print(os.system("clear"))
print(os.system("pwd"))
print(os.system("ls"))
# os.system is to run you os command, if it is zero means command is success.
print(os.system("ff")) # exit status is not zero

cmd="date"
rt=os.system(cmd)
if rt==0:
    print("success")
else:
    print("failed")
