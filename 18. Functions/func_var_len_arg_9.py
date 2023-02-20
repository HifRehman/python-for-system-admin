# Variable lenght arguments in your function

'''def display(*arg): # any value like arg/data/kells or anything * means 0 or more arguments
    print(arg)
    print(type(arg))
    return None

display() # output comes in tuple
display(4)
display(4,5,6)
'''

def display(*arg):
    for each in arg:
        print(type(each))
    return None

display(4,5,6)
display("========")
display("kells")
display("hi", 4.3)
