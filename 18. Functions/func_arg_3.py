# Functions with arguments.

def get_result(value): # parameters/positional parameter
    result = value + 10 
    print(f"result is {result}")
    return None

def main():
    num = eval(input("Please provide number : "))
    get_result(num) # Arguments
    return None
main()
