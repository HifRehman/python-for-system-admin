'''
practice with findall operation:
import re
print(re.findall(pattern,text))

Rules to create pattern:
------------------------
a, X, 9 -> ordinary characters that match themselves
[abc] -> Matches a or b or c
[a-f] -> a,b,c upto f
[a-zA-Z0-9] -> Matches any letter from (a to z) or (A to Z) or (0-9)
\w -> Matches any single letter, digit or underscore
\W -> Matches any character not part of \w
\d -> Matches decimal digit 0-9
. -> Matches any single character except newline character

'''

import re
text = "This is python2. programming it is python3 easy to learn 5 57"
#my_pattern = "i[st]"
#my_pattern = "[a-d]"
#my_pattern = "a"
#my_pattern="\w"
#my_pattern="\w\w"
#my_pattern="\w\w\w"
#my_pattern="\W"
#my_pattern="\d"
#my_pattern="python\d"
#my_pattern="\d\d"
#my_pattern="."
#my_pattern=".."
#my_pattern="..."
my_pattern="\."
#print(len(re.findall("is",text)))
print(re.findall(my_pattern,text))


text_2 = "This is my ip of the server : 255.100.102.104 2412417267786841"
#pat = "\d\d\d.\d\d\d.\d\d\d.\d\d\d"
pat = "\d\d\d\.\d\d\d\.\d\d\d\.\d\d\d"
#pat = "\w\w\w.\w\w\w.\w\w\w.\w\w\w"
print(re.findall(pat,text_2))

