# #Example 1
# def greet(name,age):
# 	print(f"Hi {name}")

# #example 2
# def even(num):
# 	if(num%2 ==0):
# 		print(f"{num}Even number")
# 	else:
# 		print(f"{num}Odd number")
# even(7)

# #example 3
# def prime(num):
# 	for i in range(2,(num//2)+1):
# 		if(num%i==0):
# 			print(f"{num} Not prime ")
# 			break
# 	else:
# 		print(f"{num} is prime number")
# prime(23)

# #keyword
# #default keyword
# def greet(name,age,place = "Alappuzha"):
# 	print(f"Hi,i am {name}..am {age} years old")
# 	if place:
# 		print(f"am from {place}")

# greet("Biona",21,'kottayam')
# greet("Apsa",22)

#  *args

# def add(*args):
# 	sum =0
# 	for i in args:
# 		sum +=i
# 	print(sum)

# add(1,3,5,7,9)

# store values as dictionary and we can pass so many arguments
# def greet(**args):
# 	print(args["name"])

# greet(name = "apsa", age = 22, place = "alappuzha")

#return 

# def add(*args):
# 	sum =0
# 	for i in args:
# 		sum +=i
# 	return (sum)

# s = add(1,3,5,7,9)
# print(s)

#reccursion

# def fact(n):
# 	if(n==1):
# 		return n
# 	else:
# 		return n*fact(n-1)
	
# print("Factorial :",fact(4))

#Fibonacci using reccursion

def fib(n):
	if n==0:
		return 0
	elif n ==1:
		return 1
	else:
		return fib(n-1)+fib(n-2)
	
n = int(input("Enter the string length:"))
print("fibonacci series :",end = " ")
for i in range(n):
	print(fib(i), end = " ")