'''
search -> It looks throughout the entire string and returns the first match.
match -> This will only work if your matched string at 0 index otherwise it won't work even if u mention re.M
        re.I will work

'''
import re
text = "python This is for python and there are two major version python2 and python3 in future python4"
# this work with multiline as well.

pattern = r"\bpython[23]?\b" # r"\bpython\d\b"
# print(re.findall(pattern, text))
match = re.search(pattern,text)
if match:
    print(match)
    print("match from ur pattern: ", match.group())
    print("Starting index: ", match.start())
    print("Starting index: ", match.end()-1)
    print("Length", match.end()-match.start())
else:
    print("No match found")

print(re.match(pattern, text, re.I))