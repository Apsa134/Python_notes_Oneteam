#Bubble sort

#num = [19,2,1,23,8]  #here we predefined the list
n = int(input("Enter the length:"))
print("Enter the numbers")
num = []
#num = [0]*n  #indexing the space for the list to enter the numbers as per the given length
for k in range(1,n+1):
	numb = int(input(f"Enter the {k} number: "))
	num =  num+[numb]
	#num[k] = int(input())  #other way
print(f"Unsorted list:{num}")

for i in range(n-1):
	for j in range(n-i-1):
		if(num[j]>num[j+1]): 
			num[j],num[j+1] =num[j+1],num[j] #swap the numbers
print(f"Sorted list:{num}")