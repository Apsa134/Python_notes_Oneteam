#Example 1
def greet(name,age):
	Print(f"Hi {name}")




#example 2
def even(num):
	if(num%2 ==0):
		print(f"{num}Even number")
	else:
		print(f"{num}Odd number")


even(7)

#example 3
def prime(num):
	for i in range(2,(num//2)+1):
		if(num%i==0):
			print(f"{num} Not prime ")
			break
	else:
		print(f"{num} is prime number")


prime(23)

#keyword
#default keyword
def greet(name,age,place = "Alappuzha"):
	print(f"Hi,i am {name}..am {age} years old")
	if place:
		print(f"am from {place}")

greet("Biona",21,'kottayam')
greet("Apsa",22)