def display(a=1):
    print("The value of a is : ",a)
    return None

display(6)
display()

def add_num(a=0,b=0):
    result = a+b
    print("addition : ",result)
    return None

add_num(4)
add_num()
add_num(4,5)

def work_on_some(user="root"):
    print(f"working with {user}")
    return None
work_on_some("kells")
work_on_some()