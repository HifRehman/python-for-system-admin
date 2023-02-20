
import os
class Tomcat: # this is like preparing some template in (to group related function)
    def get_details_for_each_tomcat(self,server_xml): # Now this function is method in terms of class with one extra keyword self
        self.tcf = server_xml
        self.th = os.path.dirname(os.path.dirname(server_xml))
        return None
    
    def display_details(self):
        print(f'The tomcat config file is : {self.tcf}\n The tomcat home is: {self.th}')
        return None

def main():
    tomcat7 = Tomcat()
    tomcat9 = Tomcat()

    tomcat7.get_details_for_each_tomcat("/home/automation/tomcat7/conf/server.xml")
    # somewhere in memory it is going to create like self is calling itself like tomcat7
    # get_details_for_each_tomcat("tomcat7","/home/automation/tomcat7/conf/server.xml")
    tomcat9.get_details_for_each_tomcat("/home/automation/tomcat9/conf/server.xml")
    # get_details_for_each_tomcat("tomcat9","/home/automation/tomcat9/conf/server.xml")
    # here dynamically creating variable
    # print(tomcat9.tcf)
    # print(tomcat9.th)
    # print(tomcat7.tcf)
    # print(tomcat7.th)
    tomcat7.display_details()
    tomcat9.display_details()
    return None

if __name__=="__main__":
    main()