'''
Constructor is a special method that is called by default whenever you create an object from a class.

'''

class Emp:
    count=0
    def __init__(self):
        Emp.count=Emp.count+1
        print("This is an init method")
    def display(self):
        print("This is a display method")

emp1 = Emp()
emp2 = Emp()

# emp1.display()
# emp2.display()

print("Number of object created from Emp class are: ", Emp.count)