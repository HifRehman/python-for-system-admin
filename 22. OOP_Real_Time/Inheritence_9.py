'''
Inheritence is a mechanism that allows us to create a new class known as child class
that is based upon an existing class - the parent class.

Advantage : This saves you from duplicating a lot of code.

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
class Apache(Tomcat):
    def __init__(self,home,ver):
        self.home = home
        self.version = ver
        return None

tom_ob = Tomcat("/home/tomcat", '7.6')
apa_ob = Apache("/etc/httpd", '2.4')

tom_ob.display()
apa_ob.display()