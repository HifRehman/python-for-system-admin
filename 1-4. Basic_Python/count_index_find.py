x = 'Python is an easy leanguage and it is easy'
print(x.count('is'))
print(x.count('i'))

print(x.index('P'))
print(x.index('is'))
print(x.index('is',8)) # it means check after index value 8
#better operation is find operation.

print(x.find('is')) # it will search for the first one only
print(x.find('is',8)) # find after index value 8
print(x.find('is',36)) # find after index value 36

