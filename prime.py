num = int(input("Enter the number:"))
flag =0
for i in range(2,num): #for i in range(2,(num//2)+1):# this will also work
	if(num%i ==0):
		flag =1
		break
	else:
		continue

if(flag==1):
	print("Not prime")
else:
	print("Prime")

