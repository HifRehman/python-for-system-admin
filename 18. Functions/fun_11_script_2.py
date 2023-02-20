import fun_11_script_1
#print(dir(fun_11_script_1))

def mult(x,y):
    print(f"multiply of {x} and {y} is {x*y}" )
    return None
'''
x=6
y=5

fun_11_script_1.add(x,y)
#fun_11_script_1.sub(x,y)
#mult(x,y)

# while running above getting extra output from script1 which is the logic of scrip1 which we don't need
'''
def main():
    x=6
    y=5
    fun_11_script_1.add(x,y)
    #fun_11_script_1.sub(x,y)
    # #mult(x,y)
if __name__=="__main__":
    main()

'''
__name__ variable:- basically if the name of the script is equal to main then it will execute the main function
so we use this __name__=="__main__" so that in another script if we import the script then it do not execute extra 
code except what we are trying to use.

'''
#print(__name__)