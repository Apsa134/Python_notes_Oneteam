#Example for if-else statement
Age = int(input("Enter your age:"))
if Age >= 18 :
	print("Eligible for voting")
else:
	print("Not eligible for voting")

#Example for if(-elif-else statement
Age = int(input("Enter your age:"))
if Age < 18 :
	print("Young")
elif Age >= 18 and  Age < 60:
	print("Adult")
else:
	print("Old")

#example odd or even
num = int(input("Enter a number:"))
if num % 2 == 0 :
	print("Even number")
else:
	print("Odd number")
# Menu driven example
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("Choose anyone\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division")
choice = int(input("Enter your choice: "))
if choice == 1:
	print("Sum:", num1 + num2)
elif choice == 2:
	print("Difference:", num1 - num2)
elif choice == 3:
	print("Product:", num1 * num2)
elif choice == 4:
	print("Quotient:", num1 / num2)
else:
	print("Invalid choice")

