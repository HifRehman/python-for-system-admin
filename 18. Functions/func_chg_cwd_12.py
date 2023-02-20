import os
# print(os.getcwd())
# os.chdir("/etc")
# print(os.getcwd())
#os.chdir("/root")
# print(os.getcwd()) # it will give permission error
# PermissionError: [Errno 13] Permission denied: '/root'

#os.chdir("/etc/abc") # it will give file not found exception
# FileNotFoundError: [Errno 2] No such file or directory: '/etc/abc'
#os.chdir("/etc/sysctl.conf")
# NotADirectoryError: [Errno 20] Not a directory: '/etc/sysctl.conf'

def main():
    path = input("Enter path to change directory : ")
    print("The CWD is : ", os.getcwd())
    try:
        os.chdir(path)
        print("Now you new CWD is : ", os.getcwd())
    except FileNotFoundError:
        print("Invalid path pls check again :)")
    except NotADirectoryError:
        print("Not a Directory, Check Again :)")
    except PermissionError:
        print("You do not have the permission :)")
    except Exception as e:
        print(e)
    return None

if __name__=="__main__":
    main()