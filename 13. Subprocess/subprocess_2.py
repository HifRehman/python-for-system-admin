import subprocess

cmd=['java', '-version']
# cmd="java -version"
sp=subprocess.Popen(cmd,shell=False,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)
rc=sp.wait()
o,e=sp.communicate()
# print(o)

if rc==0:
    for each_line in e.splitlines():
        if "version" in each_line:
            print(each_line.split())
else:
    print("command was failed: " ,e)