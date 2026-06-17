	# finding the frequency of characters in the string

n = input("Enter the string:")
d = {}

for i in n:
	if i in d:
		d[i]=d[i]+1
	else:
		d[i]=1

for m in d:
	print(f"{m}={d[m]}")