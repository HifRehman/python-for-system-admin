'''
Exception Handling for Known Exceptions.
If you already know the exception then you can directly you can manage them.

'''
 
#print(a) # NameError
#print(4+"string") # TypeError
#open("xyz.txt") # FileNotFoundError
#print(5/0) # ZeroDivisionError

try:
    print(a)
    
except NameError:
    print("Variable is not defined")

try:
    print(4/0)
    print(4+"hi")
except TypeError:
    print("Adding number and string is not possible")
except ZeroDivisionError:
    print("Division with Zero is not possible")
except Exception as e:
    print(e)
finally:
    print("Finally this will execute")


'''

try:
	print("This is try block")
	import fabric
	print(a)
	#print(4+"hi")
	#open('asdfas.txt')
	#print(5/0)
	
except FileNotFoundError:
	print("File is not present to open it")
except NameError:
	print("Variable is not defined")
except TypeError:
	print("Adding number and string is not possible")
except ZeroDivisionError:
	print("Division with zero is not possible")
except ModuleNotFoundError:
	print("Please install fabric to use it")
except Exception as e:
	print(e)
finally:
	print("Finally this will executes")

'''
