# python built-in function.

import datetime
# import pytz

# print(dir(datetime))
# # print(dir(datetime.datetime))
# print(datetime.datetime.today())
# print(datetime.datetime.now()) # helpful to get info about other timezone
# ist = pytz.timezone('Asia/Kolkata')
# print(datetime.datetime.now(ist))

# print(datetime.datetime.now().year)
# print(datetime.datetime.now().day)
# print(datetime.datetime.now().min)
# print(datetime.datetime.now().hour)
# print(datetime.datetime.now().second)

# print(datetime.datetime.now().strftime("%y-%m-%d"))
# print(datetime.datetime.now().strftime("%Y-%m-%d"))
# print(datetime.datetime.now().strftime("%c"))
# strftime.org -> where u can check the symbol or format

print(datetime.datetime.fromtimestamp(1555555555))
print(datetime.datetime.max)

from datetime import datetime
print(datetime.now())


