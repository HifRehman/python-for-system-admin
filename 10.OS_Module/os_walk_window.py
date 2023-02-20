import os
import string
pd_names=string.ascii_uppercase
vd_names=[]
for each_drive in pd_names:
    if os.path.exists(each_drive+":\\"):
        # print(each_drive)
        vd_names.append(each_drive+":\\")
print(vd_names)


