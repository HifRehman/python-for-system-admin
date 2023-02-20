import os
import datetime
import sys

req_path = input("Enter your path :- ")
age = 2
if not os.path.exists(req_path):
    print("Please provide the correct path.")
    sys.exit()
if os.path.isfile(req_path):
    print("Please provide the directory path.")
    sys.exit()

today = datetime.datetime.now()
for each_file in os.listdir(req_path):
    each_file_path=os.path.join(req_path,each_file)
    if os.path.isfile(each_file_path):
        file_cre_date = datetime.datetime.fromtimestamp(os.path.getctime(each_file_path))
        dif_days = (today - file_cre_date).days
        if dif_days > age:
            print(each_file_path,dif_days)