#Example 1
for i in range(5):
	for j in range(i+1):
		print("*",end =(" "))
	print("")

#Example 2
for i in range(1,6):
	print(" *"*i)
#Example 3
for i in range(1,6):
	print(" "*(6-i)+"*"*i)
# Example 4
for i in range(1,6):
	print(" "*(6-i)+"* "*i)

#example 5
rows = 4
for i in range(1,rows+1):
	num = i
	for j in range(1,i+1):
		num = i*j
		print(num,end = " ")
	print("")
	