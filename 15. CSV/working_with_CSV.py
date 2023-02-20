'''
CSV -> comma separated values.
It is a simple file format used to store tabular data, such as a spreadsheet/excel or database.

'''
import csv
# req_file = "info.csv"
# fo = open(req_file,"r")
# content = fo.readlines()
# fo.close()

# for each in content:
#     print(each.strip("\n"))
#     print(each.strip("\n")).split(",")

req_file = "info.csv"
fo = open(req_file,"r")
data=csv.reader(fo,delimiter=",")
# print(list(data))

#print(f"The header is: \n {list(data)[0]}")
header = next(data)
print(f"The header is : ", header)
print("The number of rows are : ", len(list(data)))

# for each in data:
#     print(each)
fo.close()