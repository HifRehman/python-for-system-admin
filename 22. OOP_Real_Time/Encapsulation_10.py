'''
Encapsulation: 

- Using OOP in Python, we can restrict access to methods and variables.
- This prevent data from direct modification which is called encapsulation.

'''

class Person(object):
    def assign_name_and_age(self,name,age):
        self.name = name
        self.__age = age
        self.__display()
        return None
    def __display(self):
        print(self.name,self.__age)
        return None

per1 = Person()
per1.assign_name_and_age('kells', 32)

#per1.display()
#print(per1.name)
#print(per1.__age) # not from outside of the class 