class Animals: #Parent class
	def get_details(self,n):
		self.name = n
class Cats(Animals): # Child class
	def info(self):
		print(self.name)

cat1 = Cats() # object creation
cat1.get_details("Undu") 
cat1.info()


##Using init

class Animal:
	def __init__(self,n):
		self.name = n

class Cat(Animal):
	def __init__(self,n):
		super().__init__(n) #for accessing the methods in the parent class 
		print(self.name)

cat1 = Cat("Eva")

