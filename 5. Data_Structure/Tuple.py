# Difine a tuple.
empty_tuple = ()
my_tuple = (3,5,1)
print(my_tuple)

my_tuple_2 = (1,2,4,[5,6,7],9,0)
print(my_tuple_2)
print(my_tuple_2[3][2])

# Tuples & Strings are immutable.
print(dir(my_tuple_2))
print(my_tuple_2.count(1))
print(my_tuple_2.index(4))
print(len(my_tuple_2))
print(my_tuple_2[2:])

x=5,
print(type(x))