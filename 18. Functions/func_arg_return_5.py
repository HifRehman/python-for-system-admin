def get_add(p,q):
    add = p + q
    #print(f"addition is : {add}")
    return add

def get_sub(m,n):
    sub = m - n
    #print(f"substraction is : {sub}")
    return sub

def main():
    a = eval(input("first value : "))
    b = eval(input("second value : "))
    add_result = get_add(a,b)
    print(f"addition is : {add_result}") 
    sub_result = get_sub(a,b)
    print(f"sub is : {sub_result}")

main()