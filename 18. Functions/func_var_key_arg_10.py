# Functions with Variable lenght keyword based arguments

'''def display(a,b):
    print(a)
    print(b)
    return None
display(4,5)
display(b=5,a=4)
'''

def display(**karg): # keyword based argument means which have key and value (dictionary)
    print(karg)
    return None
#display(4,5) # this won't work no keyvalue
display(b=5,a=4)
display(a=3,b=6,c=8)
display(x=5,y="HI",z=6.7,user="root")

# combination with normal arg and karg

def display(p,**karg):
    print(p)
    print(karg)
    return None
#display(4,5) # this won't work no keyvalue
display(77,x=5,y="HI",z=6.7,user="root")