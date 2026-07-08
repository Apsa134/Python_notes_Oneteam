#runtime polymorphism  using abstraction
from abc import abstractmethod,ABC
class A(ABC):
	@abstractmethod
	def greet(self):
		print("Hi from A")

class B(A):
	def greet(self):
		print("Hii from B")

class C(A):
	def greet(self):
		print("Hii from C")

# o = A()
# o.greet() #cant do this because it is the parent abstract class, so can't create the abject
ob =B()
ob.greet()
oc = C()
oc.greet()


#without abstraction

class A():
	def greet(self):
		print("Hi from A")

class B(A):
	def greet(self):
		print("Hii from B")

class C(A):
	def greet(self):
		print("Hii from C")

o = A()
o.greet()
ob =B()
ob.greet()
oc = C()
oc.greet()
