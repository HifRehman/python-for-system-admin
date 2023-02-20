# class Emp:
class Emp(object):
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        self.display()
        return None
    def display(self):
        print(f"The name is: {self.name}\nThe salary is: {self.salary}")
        return None

emp1 = Emp("Kells", 90000)
# emp1.display()

emp2 = Emp("Hif", 50000)
# emp2.display()

### 98. Simple python script without and with oops concepts ## Need to revisit this video later