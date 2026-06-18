#list comprehension

#example 1
a = [9,16,25,36]
res = [val **(1/2) for val in a]
print(res)

#example 2
num = [n for n in range(2,45) if n%5==0]
print(num)