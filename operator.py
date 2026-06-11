# # Arithematic Operators
# a=6
# b=4
# print(a+b) #Addition
# print(a-b) #Subtraction
# print(a*b) #Multiplication
# print(a/b) #Division
# print(a//b) #Floor Division
# print(a**b) #Exponentiation	
# print(a%b) #Modulus
'''
#Assignment Operators
a=10
a+=5 #a=a+5	
print(a)
a-=5 #a=a-5
print(a)
a*=5 #a=a*5	
print(a) 
a/=5 #a=a/5
print(a)
b=20	
b//=2#b=b//2
print(b)
'''
'''#Comparison Operators

a,b = 10,20
print(a==b) #Equal to
print(a!=b) #Not Equal to
print(a>b) #Greater than
print(a<b) #Less than
print(a>=b) #Greater than or equal to
print(a<=b) #Less than or equal to
'''
#Logical Operators
# age = 25
# nationality = "Indian"
# print(age > 18 and nationality == "Indian") #Logical AND
# print(age > 18 or	nationality == "Indian") #Logical OR
# print(not(age > 18 and nationality == "Indian")) #Logical	NOT

#Membership Operators
#print(25 in [10, 20, 25, 30] )

#Identity Operators
a = [1, 2, 3]
b = a
print(a is b) #True, because a and b refer to the same object in memory

c = [1, 2, 3]
print(a is c) #False, because a and c are different objects in memory, even though they have the same content

p = "Apsa"
q = "Apsa"
print(p is q) #True, because Python optimizes memory for string literals, so p and q refer to the same string object in memory