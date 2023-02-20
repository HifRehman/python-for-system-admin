import re
# x = 5
# print(id(x))


# x = int(input("Enter x "))
# print(type(x))

# y = eval(input("Enter y: "))
# print(type(y))

# world = "Hif World"
# print(world.lower())
# print(world.upper())
# print(world.title())
# print(world.swapcase())
# print(world.capitalize())
# print(world.casefold())

# txt = "I could eat bananas all day"
# x = txt.partition("bananas")
# print(x)



# host1_x = host1.partition("ztds")
# print(host1_x)

# h1 = re.split('; |, |\*|\n',host1)
# print(h1)

# a="Beautiful, is; better*than\nugly"
# a1 = re.split('; |, |\*|\n',a)
# print(a1)

my_str = "This is the new era be ready with latest technology with Hif"
print(my_str.startswith('T'))
print(my_str.startswith('p'))
print(my_str.endswith('Hif'))
print(my_str.islower())
print(my_str.isupper())
print(my_str.istitle())
print(my_str.isspace())
print(my_str.isalpha())
print(my_str.isnumeric())
