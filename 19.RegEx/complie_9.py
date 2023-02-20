# Compile operation of re module.
import re
my_str = "This is about python and Python is very easy and we are having python2 vers and Python2 vers"
my_pat = r'\bpython[23]?\b'
'''
print(re.search(my_pat,my_str))
print(re.findall(my_pat,my_str,flags=re.I))
print(re.split(my_pat,my_str))
'''

pat_ob = re.compile(my_pat,flags=re.I)
print(pat_ob) # this is an object now u can directly perform your operation on your object
print(pat_ob.search(my_str))
print(pat_ob.findall(my_str))

# whenever using same pattern in different places in your code then you can create compile object and on that object
# u can perform operation, so your code can be efficient

# re.findall(my_pat, my_str)  ====>> re.compile(my_pat).findall(my_str)
