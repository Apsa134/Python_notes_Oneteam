#Normal copy

n = [["Apsa",22],["Abhiram",21]]
k = n 
k[0][1] = 25
print(k)
print(n)

#deep copy

import copy
a = [["Oneteam", 3],["kochi",5]]
b = copy.deepcopy(a)
b[0][0] = "python"
print(b)
print(a)

#shallow copy

import copy
a = [["Oneteam", 3],["kochi",5]]
b = copy.copy(a)
b[0][0] = "python"
print(b)
print(a)