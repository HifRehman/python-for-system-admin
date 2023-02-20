'''
The regex is a procedure in any language to look for a specified pattern a given text.
The different operations in python re are:

match()
search()
findall()
finditer()
sub()
split()
compile()
etc

re is the module name.
Syntax:

- re.search(pattern, text)
- re.match(pattern, text)
- re.finditer(pattern, text)
- re.findall(pattern, text)

-> Pattern is a sequence of characters, which represent multiple strings.
Example:

"Python"
"Python[23] -> "Python2" "Pyhthon3"
r"Python" or r"Python[23]"


'''
import re
my_str = "python is simple and it easy"
print(my_str.split("is"))
print(my_str.split("it"))

print(re.split("i[st]",my_str))