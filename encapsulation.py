class Employee:
    def __init__(self, name,position, salary):
        self.name = name          # public attribute
        self._position = position #protected
        self.__salary = salary    # private attribute

emp = Employee("Fedrick","Manager", 50000)
print(emp.name)       
print(emp._position)
#print(emp.__salary)#This throws an error because salary is private
#print(emp._Employee__salary) #it doesnot show any error
