import os
def get_details_for_each_tomcat(server_xml):
    global tcf, th
    tcf = server_xml
    th = os.path.dirname(os.path.dirname(server_xml))
    return None
def display_details():
    print(f'The tomcat config file is : {tcf}\n The tomcat home is: {th}')
    return None



def main():
    tomcat7 = "/home/automation/tomcat7/conf/server.xml"
    tomcat9 = "/home/automation/tomcat9/conf/server.xml"
    get_details_for_each_tomcat(tomcat7)
    display_details()
    get_details_for_each_tomcat(tomcat9)
    display_details()

if __name__=="__main__":
    main()

