'''
^ - start of the string (and start of the line incase of multiline string)
$ - end of the string (and newline character incase of multiline string)
\b - empty string at the beginning or end of a word
\B - Empty string not at the beginning or end of a word
\t, \n, \r -> matches tab, newline, return respectively
'''

import re
text = "it is a python and it is   easy to learn islearnis   \n "
#my_pat = '^i[st]'
#my_pat = 'learn$'
#my_pat = r'\blearn' # r rawstring it will ignore special character
#my_pat = r'\Blearn\B'
my_pat=r"\n"
print(re.findall(my_pat,text))