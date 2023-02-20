def my_func1():
    x = 20 # local variable
    print("Welcome to the funk master flex ")
    print(x)
    my_func2(x)
    return None

def my_func2(x): # parameter
    print("Thank you everybody")
    print(x)
    return None
x = 10

def main():
    #global x
    x = 10
    my_func1()
    my_func2(x) # argument
    return None

main()