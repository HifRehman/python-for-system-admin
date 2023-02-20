import re
my_str = "This is python and we are having python2 and python3 version"
my_patt = r'\bpython[23]?\b'
#print(re.match(my_patt,my_str)) # re.match look for first word
#print(re.search(my_patt,my_str))
#print(re.findall(my_patt,my_str)) # findall give list
#print(len(re.findall(my_patt,my_str)))

# finditer gives some object and index value
print(re.finditer(my_patt,my_str)) # it will give some object always

for each_ob in re.finditer(my_patt,my_str):
    print(f'The match is: {each_ob.group()} Starting index: {each_ob.start()}, Ending index {each_ob.end()-1}')
