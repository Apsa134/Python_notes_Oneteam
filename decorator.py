#decorator
def my_dec(fun):
	def wrapper():
		print("Hii")
		fun()
	return wrapper
@my_dec
def greet():
	print("Hello")

greet()
# f = my_dec(greet)
# f()

#Example 1

def dec(fun):
	def wrap(a,b):
		if a>b:
			return fun(a,b)
		else:
			print ("A must be greater than b")
	return wrap

@dec
def divide(a,b):
	print (a//b)

divide(30,32)