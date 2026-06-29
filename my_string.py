# String methods

# 1. lower
Name = "apsa Biju"
print(Name.lower())

#2.Upper
print(Name.upper())

#3.split
print(Name.split())

 #4.join
print("_".join(Name))

#5.count
print(Name.count("a"))

#6.index

print(Name.index("B"))
#7.swapcase

a = "I love Python"
swapped_text = a.swapcase()
print(swapped_text)

#8.strip

s = "  ApsaBiju  "#removed the white space in the front and back
res = s.strip()
print(res)

#9.partition
m = "Hello Developers... Hii"
print(m.rpartition(" "))

#10.Capitalize
n = "abhiram"
print(n.capitalize())
