print('a' < 'b')
print(ord('a'))
print(ord('b'))
print(ord('-'))
print(ord('&'))

print(chr(45))
print(chr(90))

print('aa' < 'b')

print ('aab' > 'bbc') # compare char by char

# Identity and Membership Operator.

'''
Identity operators are used to find the type of: class/type/object.
They are two types of Identity operators:
is
is not
'''

x = 5
st = "hi"
y = 10

print(type(x) is type(y))
print(type(x) is not type(st))

'''
Membership operators are used to validate the membership of a value.
in
not in
'''

h = [4,5,6,7]
print(6 in h)

valid_version = ['1.6', '1.7', '1.8']
host_version = '1.5'

print(host_version in valid_version)

if host_version in valid_version:
    print("Host deployed on latest version")
else:
    print("Host is deployed on older version")

db_user = ['db_admin', 'db_conf', 'db_install']
random_user = 'db_admin'

if random_user in db_user:
    print("yes is a valid user")
else:
    print("invalid user")

# Logical operator
'''
logical operator are useful to combine multiple conditions.
they are of 3 types
- and
- or
- not
'''

all([2<4, 5<6]) # all = and operator

any([5>2, 2>6]) # any = or operator

