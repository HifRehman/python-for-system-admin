import os
# path=input("ENter the path : ")
# fd_list=os.listdir(path)
# # print(fd_list)
# p1=fd_list[:]
# p2=fd_list[1]

# print(p1)
# # print(p2)

path=input("ENter the path : ")
lsdir=os.listdir(path)
print(lsdir)

for i in lsdir:
    if os.path.isfile(i):
        print(f"is a file")

