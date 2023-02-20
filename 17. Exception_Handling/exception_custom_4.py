'''
Creating Custom Exceptions.

raise -> Used to raise an existing exceptions.
assert -> Used to create an AssertionError.

'''

#raise Exception("This is an exception")
#raise NameError("Variable is not defined")

a = 23
# if age > 30:
#     print("Valid age")
# else:
#     raise ValueError("Age is less than 30")

#assert 4<3 

age = 25

try:
    assert age > 30
    print("valid age")
except AssertionError:
    print("Raised with assert because age is less than 30")
except:
    print("Exception occured")