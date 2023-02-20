'''
Constructor :- is a special method that is called by default whenever you create an object from a class.

Destructor:- are called when an object gets destroyed.

In Python, destructor are not needed as much needed in C++ because Python has a garbage collector that handles memory 
management automatically.

'''
class Person(object):
    def __init__(self,name,age) -> None:
        print("an object has been created")
        self.name = name
        self.age = age
        return None
    
    def __del__(self): ## No need to write this method python take care itself. but if write good.
        print("object has been deleted")
        return None

per1 = Person('Kells',32)