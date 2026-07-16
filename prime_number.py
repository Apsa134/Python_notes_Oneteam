def is_prime(num):
    if num < 2:
        return False

    for i in range(2, int(num //2) + 1):
        if num % i == 0:
            return False

    return True




n = int(input("Enter the range:"))
count = 0
number = 2

while(count<n):
	if(is_prime(number)):
		print(number,end = " ")
        count += 1
        number += 1






