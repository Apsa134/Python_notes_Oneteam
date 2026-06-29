# Dictionary Methods
std = {"name":"Apsa","age":22,"place":"Alappuzha"}

# 1. get
print(std.get("age"))

# 2. pop

print(std.pop("age"))
print(std)

# 3. popitem
print(std.popitem())
print(std)

# 4.update
std.update({"Hobbies":["chess","music"]})
print(std)
