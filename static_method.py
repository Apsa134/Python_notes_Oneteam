class Person:
    def __init__(self, age):
        self.age = age

    @staticmethod
    def is_adult(age):
        return age >= 18

print(Person.is_adult(20))
p = Person(16)
print(p.is_adult(p.age))