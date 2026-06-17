
#Example of while loop to print numbers from 1 to 5
count = 1
while count <=5:
	print(count, end=" ") #Prints numbers in the same line with a space
	count += 1 #count = count + 1	

#factorial of a number
num = int(input("Enter a number: "))
fact = 1
while num > 0:
	fact*= num
	num -=1
print("Factorial:", fact)

#fibanocci series using while loop
n = int(input("Enter the string length: "))
a=0
b =1	
count = 0
while count < n:
	print(a , end = " ")
	c = a+b
	a,b = b,c
	count+=1


#break,continue and pass statements

while True:
	num1 = int(input("Enter first number: "))
	num2 = int(input("Enter second number: "))
	print("Choose anyone\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Exit")
	choice = int(input("Enter your choice: "))
	if choice == 1:
		print("Sum:", num1+num2)
	elif choice == 2:
		print("Difference:", num1 - num2)
	elif choice == 3:
		print("Product:", num1 * num2)
	elif choice == 4:
		print("Quotient:", num1 / num2)
	else:
		print("Invalid choice")
	print("Do you want to continue? (yes/no):")
	ans = str(input())
	if ans == "no":
		print("Exiting ....")
		break	

#Example using list
list1 = ["Apple","Orange","Banana","Cherry","Avacado"]
for i in list1:
	if i[-1] in "AEIOUaeiou":
		print(i)

#list slicing

list2 = ["Apsa","Abhiram","Biona","Athulya","Ebin"]
print(list2[0:3])
print(list2[3:6])
