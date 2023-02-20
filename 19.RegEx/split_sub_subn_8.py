# split and sub, subn operations of re module
import re

#print(help(re.split))
my_str = "This is about python and python is very easy and we are having python2 vers and Python2 vers"
my_patt = r'python[23]?'
print(re.split(my_patt,my_str))
print(re.split(my_patt,my_str,flags=re.I))
print(re.split(my_patt,my_str,maxsplit=3,flags=re.I))

#print(help(re.sub))

print(re.sub(my_patt,'jython',my_str)) # this is not going to disturn original string

print(re.sub(my_patt,'jython',my_str,count=2,flags=re.I))
print(re.subn(my_patt,'jython',my_str,count=2,flags=re.I)) # how many place it is going to change will give that value





