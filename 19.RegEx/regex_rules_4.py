'''
{2} exactly 2 times
{2,4} 2,3 or 4 times
{2,} 2 or more times
+ one or more
* 0 or more times
? once or none(lazy)

'''
import re
'''text = "This is a python and python3 pythonnnn aaaaaaaa hahahahahhhh"
#my_pat = r"\bpython\b"
#my_pat = r"\bpython{4}\b"
#my_pat = r"\ba{8}\b"
print(re.findall(my_pat,text))
'''
text2 = "xaz asdfa sdf xaazz xaaaaaaaz xaaaaz"
#my_pat = r'\bxa{1,4}z\b'
#my_pat = r'\bxa{2,}z\b'
#my_pat = r'xa{1,}z'
#my_pat = r'xa+z'
#my_pat = r'xa*z'
my_pat = r'xa?z'
print(re.findall(my_pat,text2))
