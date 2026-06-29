#Set Methods

s1 = {1, 4, "Apsa",56,2}
s2 = {4,"Abhiram", 56}

# 1. Add
s1.add(23)
print(s1)

# 2.Remove
s1.remove(23)
print(s1)

# 3. Union 
print(s1.union(s2))

# 4. Intersection
print(s1.intersection(s2))

# 5. Is subset

print(s2.issubset(s1))

#Is superset

print(s2.issuperset(s1))