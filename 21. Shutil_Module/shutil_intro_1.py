'''
Python shutil module provide a number of high level operations on files and directories like copy, move, remove etc.

copy related :- 'copy', 'copy2', 'copyfile', 'copyfileobj', 'copymode', 'copystat', 'copytree'
'''
import shutil
#print(dir(shutil))
# copy operation

src = "/home/ansadmin/py-for-sys/Total"
dest = "/home/ansadmin/py-for-sys/Shutil_Module/shutil_example.txt"
#shutil.copyfile(src,dest) # permission will be different
#shutil.copy(src,dest) # same permission 
#shutil.copy2(src,dest) # same metadata like permission and datastamp
#shutil.copymode(src,dest) # to give the same permission as src file but no copy
#shutil.copystat(src,dest) # 

# f1 = open('xyz.txt', 'r')
# f2 = open('pqr.txt', 'w')
# shutil.copyfileobj(f1,f2)

# copytree is usefull to copy entire directory recursively

src = "/home/ansadmin/py-for-sys/Shutil_Module/"
#shutil.copytree(src, '/tmp/shutil')
shutil.rmtree('/tmp/shutil')