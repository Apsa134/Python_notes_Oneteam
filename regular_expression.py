import re
s= "apsabiju04@gmail.com"
m = re.findall(r'[A-Z1-9]+@+[]',s)
print(m)
# print(m.start())
# print(m.end())