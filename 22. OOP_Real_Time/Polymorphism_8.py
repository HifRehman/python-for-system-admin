'''
Polymorphism allow us to define same methods in different classes.

This process is also known as Method overriding.


'''

class Tomcat(object):
    def __init__(self,home,ver):
        self.home = home
        self.version = ver
        return None
    def display(self):
        print("This is from tomcat class")
        print(self.home)
        print(self.version)
        return None
class Apache(object):
    def __init__(self,home,ver):
        self.home = home
        self.version = ver
        return None
    def display(self):
        print("This is from apache class")
        print(self.home)
        print(self.version)
        return None

tom_ob = Tomcat("/home/tomcat", '7.6')
apa_ob = Apache("/etc/httpd", '2.4')

tom_ob.display()
apa_ob.display()