# #for loop in string
# for k in "Apsa":
# 	print(k)

# 	#iteration in for loop
# for i in range(1, 11,2):
# 	print(i)#iterate by 2

# #fibanocci series

# a,b = 0,1
# print(a,b)
# for k in range(6):
# 	c = a + b
# 	print(c)
# 	a,b= b,c
	
#other way to write fibanocci series
	
n = int(input("Enter the string length: "))
a=0
b =1
for i in range(n):
	print(a, end = " ")
	c = a + b
	a,b= b,c

#Multiplication table

n = int(input("Enter a number: "))
for i in range(11):
	print(f"{n} x {i} = {n*i}")#for printing all in a line without separating with commas
	
