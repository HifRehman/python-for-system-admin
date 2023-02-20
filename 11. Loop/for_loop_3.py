# find all files in a directory with ext .py/.sh/.log/.txt etc...
import os

path = input("Enter your path to search .py/.sh/.log/.txt files : ")
if os.path.isfile(path):
    print(f"The given {path} is a file, pls provide directory path")
path1 = os.listdir(path)
if len(path1) == 0:
    print("given path is empty")
else:
    path2 = input("please enter the ext :- .py/.sh/.log/.txt ")
    req_files = []
    for each_f in path1:
        if each_f.endswith(path2):
            req_files.append(each_f)
    if len(req_files) == 0:
        print(f"No files in the file.")
    else:
        print(f"Files are {req_files}")

            
    