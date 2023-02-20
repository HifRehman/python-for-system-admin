'''
Subprocess module is used to execute operating system commands.
subprocess is to execute the command and store the result into a variable.
os.system will directly run your command it will not store in the variable. when you assigned to a variable it will 
only assign the success or the failure status into the variable.
syntax:
sp=subprocess.Popen(cmd,shell=True/False,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
rc=sp.wait()
out,err=sp.communicate()

if your command is string your shell will be True, if your command is list your shell will be False.

cmd='ls -ltr'
shell=True

cmd=['ls','-lrt']
shell=False




'''


import os
import subprocess

# out = os.system("ls") # this will directly run the command.
# print(out) # it will store the exit status of the command.

# cmd = 'ls -lrt'
# cmd = 'echo $HOME'
# sp=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)
# rc=sp.wait()
# out,err=sp.communicate()

# print(f'return code : {rc}')
# print(f'output :\n{out}')
# print(f'output :\n{err}')

# command output will come in bytecode to convert this into list need to add 'universal_newlines=True'
# sp=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)
# to get your output as a list 
# print(f'output :\n{out.splitlines()}')
# print(f'output :\n{err.splitlines()}')

# when shell is False it will not open a new shell instead it will run the command in python itself.
#cmd = 'ls -lrt'.split()
# cmd=['ls', '-lrt']
# cmd = 'echo $HOME'.split()
# cmd = ['echo', '$HOME']
# sp=subprocess.Popen(cmd,shell=False,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)
# rc=sp.wait()
# out,err=sp.communicate()

# print(f'return code : {rc}')
# print(f'output :\n{out.splitlines()}')
# print(f'output :\n{err.splitlines()}')

# If your command is depend on the env variable then you have to take your shell=True, otherwise no need to take as True.
# When you take shell=False then you will save some time, when you use shell=True your python is going to open a 
# new terminal and there your python run your code and getting back the result from your shell it will take some extra time.
# when shell=False it will not open a new terminal simply it will run from your python shell.

# if shell=True then your command is a string (as your os command)
# if shell=False then your command is a list
# Note: shell=False dont work on your os env variables.

# ex: cmd = "ls -lrt" ==> shell=True
#     cmd = "ls -lrt".split() or ['ls', '-lrt'] ==> shell=False

# In windows os you have to take shell=True.




