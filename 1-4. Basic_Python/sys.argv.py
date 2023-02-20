# sys.argv returns a list of commands line arguments passed to a python script.

import sys

if len(sys.argv) != 3:
    print(f"{sys.argv[0]}' <please choose from ->>..<lower|upper|title>")
    sys.exit()

usr_str = sys.argv[1]
usr_action = sys.argv[2]

if usr_action == "lower":
    print(usr_str.lower())
elif usr_action == "upper":
    print(usr_str.upper())
elif usr_action == "title":
    print(usr_str.title())
else:
    print("Your Option is invalid")
