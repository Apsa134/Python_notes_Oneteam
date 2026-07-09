def pyramid_star():
	a = int(input("Entert the row length:"))
	for i in range(1,a+1):
		print(" " * (a - i),end = "")
		for j in range(2*i-1):
			if(j%2==0):
				print("*",end = "")
			else:
				print("#",end = "")
		print()
pyramid_star()