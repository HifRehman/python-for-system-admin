def mult_with_10(value):
    #result = value * 10
    return value*10

def main():
    num = eval(input("Enter num : "))
    mult_result = mult_with_10(num)
    print(f"Your value is : {mult_result}")

main()