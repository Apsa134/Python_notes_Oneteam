#Oops class,object,Method
class Students():
	course = "Python"

	def details(self,name,place):
		self.name = name
		self.place = place

	def display(self):
		print(f"Hi am, {self.name} am from {self.place}, My course is {self.course}")

std1 = Students()
std2 = Students()

std1.details("Apsa","Alappuzha")
std2.details("Abhiram","Kannur")

std1.display()
std2.display()

#init

class stud():
	institute = "GECW" 

	def __init__(self,name,place):
		self.name = name
		self.place = place
	def display(self):
		print(f"Hi am, {self.name} am from {self.place}, My institute is {self.institute}")

stud1 = stud("Athulya","Alappuzha")
stud2 = stud("Biona","Kottayam")

stud1.display()
stud2.display()


