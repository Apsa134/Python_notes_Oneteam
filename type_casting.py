#converting the string to integer
a = int("25")
print(type(a)) # <class 'int'>

#converting the integer to string
b = str(25)		
print(type(b)) # <class 'str'>

#converting the string to list
language = "Python"			
c = list(language)
print(type(c)) # <class 'list'>
print(c) 

#converting the string to set
d = set(language)
print(type(d)) # <class 'set'>
print(d)

#dictionary
student = dict(name = "Apsa", age = 22, city = "Alappuzha")
print(type(student)) # <class 'dict'>
print(student)