#try &except
try:
	a,b = 12,0
	print(a/b)
	print("Program executed")
except:
	print("Can't Divide, denominator is zero")
print("Program executed without failure")

#define which type of error and catch it
try :
	m,n= 12,"6"
	print(m/n)  #exception
	print("Program executed")
except ZeroDivisionError:
	print("Can't Divide, denominator is zero")
except TypeError:
	print("There is an issue in type")
except Exception as e:
	print("Error occured",e)
print("Program executed without failure")

#try except,else,finally

try :
	x,y= 12,6
	print(x/y)
	print("Program executed")
except ZeroDivisionError:
	print("Can't Divide, denominator is zero")
except TypeError:
	print("There is an issue in type")
except Exception as e:
	print("Error occured",e)
else:
	print("Program executed without failure")
finally:
	print("Finally completed")