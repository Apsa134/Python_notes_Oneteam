class Number:
	def __init__(self,a,b):
		self.num1 = a
		self.num2 = b
	
	def __add__(self, other):
		return (self.num1+other.num1,self.num2+other.num2)
	
ob1 = Number(4,7)
ob2 = Number(6,3)

print(ob1+ob2)