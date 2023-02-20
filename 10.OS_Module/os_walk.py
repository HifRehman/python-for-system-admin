import os
'''
It is used to generate directory and file names in a directory tree by walking (equivalent to find command in linux).
os.walk is going to generate a list first and that list consist of tuple and that tuple consist of three values
name of the file directory and files.
'''
path = "/home/ansadmin/py-for-sys/"
# print(list(os.walk(path)))
print ("----------------------")
# for each in list(os.walk(path)):
#     print (each)

for r,d,f in list(os.walk(path,topdown=False)):
    if len(f) != 0:
        print(r)
        for each_file in f:
            # print(each_file)
            print(os.path.join(r,each_file))
        print("===========================")
