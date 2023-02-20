# emp_dict = {}
# print(emp_dict, type(emp_dict))

# my_dict = {'fruit':'apple', 'animal':'fox', 1:'one', 'two':2}

# print(my_dict['fruit'])
# print(my_dict.get('animal'))

# # print(my_dict['three'])
# print(my_dict.get('three'))

# # print(dir(emp_dict))

# my_dict['three'] = 3
# print(my_dict)

# print(my_dict.keys())
# print(my_dict.values())
# print(my_dict.items())

# # when you do the copy a new memory location will be allocated.

# cp = my_dict.copy()
# print(id(cp), id(my_dict))

# # print(my_dict)
# new_dict = {'four': 4}
# my_dict.update(new_dict)
# print(my_dict)

# my_dict.pop('four')

# my_dict.popitem()
# print(my_dict)


# keys = ['a','e','i','o','u']

# new_dict = dict.fromkeys(keys)
# print(new_dict)

# new_dict['a'] = 'alpha'
# print(new_dict)

e_dic = {}
e_dic.setdefault('k', 45)
print(e_dic)

# basically u r trying to set a new key and if key is already there then do no disturb.

e_dic={'fruit':'apple'}
e_dic.setdefault('fruit','orange')
print(e_dic)

# from python 3.7 dict is an order collection of data before that unordered.





