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
