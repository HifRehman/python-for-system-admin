import csv
req_file="demo.csv"
fo=open(req_file,"w",newline="")
csv_writer = csv.writer(fo,delimiter=",")
'''
csv_writer.writerow(['S_No','Name', 'Age'])
csv_writer.writerow(['1','Hif', '32'])
csv_writer.writerow(['2','Gunner', '32'])
'''
my_date = [['S_No','Name', 'Age'], ['1','Hif', '32'], ['2','Gunner', '32']]

csv_writer.writerows(my_date)

fo.close()