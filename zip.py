#It just combine two list tuple set
names = ["Apsa","Abhiram","Athulya"]
marks = [80,99,95]
print(list(zip(names,marks)))#print it as list

for i,j in zip(names,marks):
	print(f"{i}={j}") #For printing seperatly