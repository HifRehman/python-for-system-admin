'''
re.I -> Ignorecase flag
re.M -> Multiline
re.X -> Verbose
re.L -> LOCALE
re.S -> DOTALL (The dot "." will match every character plus the newline)
re.U -> UNICODE 
To specify more than one of them, use | operator to connect them
ex:- print(re.findall(pattern2,text2,re.M|re.I))
'''

import re
text = "this is a string ThIs is a new THIS is kellS"
#pattern = r'this'
#print(re.findall(pattern, text,re.I))

text2 = '''this kells
This is a string
THIS is second line
thIs is third line
'''
pattern2 = r"^this"
print(re.findall(pattern2,text2,re.M|re.I))