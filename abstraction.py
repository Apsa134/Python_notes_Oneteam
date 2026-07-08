from abc import abstractmethod,ABC

class Vehicle(ABC):
	@abstractmethod
	def start(self):
		print("Hiiii")

	
	def display(self):
		pass

class Bike(Vehicle):
	def start(self):
		print("Bike starting")
	
ob = Bike()
ob.start()