'''
- Built-in function
- Generates interger as a list
syntax:
 range(start, stop, step)
 3 argument - by default (start=0, step=1)

'''
print(range(5))
print(type(range(5)))
print(list(range(5)))
print(list(range(0,20)))
print(list(range(0,20,2)))
print(list(range(10,2))) # empty
print(list(range(10,2,-1)))
print(list(range(-2,-10)))
print(list(range(-2,-10,-2)))
print(list(range(0,100,2)))

for each in range(5):
    print(each)

my_list = [2,3,4,5,'python']
print(len(my_list))
print(list(range(len(my_list))))

for each_index in range(len(my_list)):
    print(f"Index --> {each_index}: value --> {my_list[each_index]}")