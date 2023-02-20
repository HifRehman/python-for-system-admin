import platform
'''
The platform module is used to access the underlying platform's data such as hardware, os and interpreter version info.

'''

print(platform.architecture())
print(platform.machine())
print(platform.processor())
print(platform.system())
print(platform.uname())
print(platform.node())
print(platform.__doc__)
print(platform.java_ver())