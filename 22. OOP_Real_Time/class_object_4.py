'''
Concept : Class and Object Attributes

Class is a template/blueprint to create an object
Class is the combination of attributes and methods
We can define Attributes for class and objects

'''

class emp:
    count = 0
    def get_name_age_salary(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary
        self.display_details()
        #self.increae_emp_count()
        return None
    def increae_emp_count(self):
        emp.count = emp.count+1
    def display_details(self):
        print(f"The name is : {self.name}\nThe age is: {self.age}\nThe salary is : {self.salary}")
        return None

emp1 = emp()
emp2 = emp()

emp1.get_name_age_salary('Hif',32,50000)
emp1.increae_emp_count()
emp2.get_name_age_salary('Kells',32,50000000)
emp1.increae_emp_count()
#emp1.display_details()

# print(dir(emp1))
# print(dir(emp2))

#print(emp1.age)
print(emp.count)
