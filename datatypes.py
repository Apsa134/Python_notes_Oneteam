""#Numbers
a=10
print(type(a)) #int

b= 3.14
print(type(b)) #float

c = 2 + 3j
print(type(c)) #complex

#Strings
s = "Apsa"
print(type(s)) #str	
list= [1, "Apsa", 3, ["oneteam",3,"Alappuzha"], 5]
print(type(list)) #list	
print(list[3]) #Accessing nested list
print(list[3][0]) #Accessing element in nested list
tuple = (1, "Apsa", 3, ["oneteam",3,"Alappuzha"], 5)
print(type(tuple)) #tuple


tuple1 = (12)
print(type(tuple1)) # This is not tuple, it's an int
tuple2 = (12,)
print(type(tuple2)) # This is a tuple, because of the comma


#set 
s={12,"Apsa",3,"oneteam",3,"Alappuzha",5}
print(type(s)) #set
print(s) #Sets do not maintain order and do not allow duplicates

#dictionary
di={"name":"Apsa","age":25,"city":"Alappuzha","Hobbies":["coding","Chess","cooking"]}
print(type(di)) #dict
print(di) #Dictionary maintains key-value pairs
print(di["name"]) #Accessing value
print(di["Hobbies"][2]) #Accessing list in dictionary