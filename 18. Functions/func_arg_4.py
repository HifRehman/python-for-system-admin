def get_add(p,q):
    add = p + q
    print(f"addition is : {add}")
    return None

def get_sub(m,n):
    sub = m - n
    print(f"substraction is : {sub}")
    return None

def main():
    a = eval(input("first value : "))
    b = eval(input("second value : "))
    get_add(a,b)
    get_sub(a,b)

main()