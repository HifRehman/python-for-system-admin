import os
# How to do a system wide search for a file?

req_file = input("ENter your filename to search: ")
for r,d,f in os.walk("/home/ansadmin"):
    for each_file in f:
        if each_file==req_file:
            print(os.path.join(r,each_file))