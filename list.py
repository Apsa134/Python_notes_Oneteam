# Append

My_list = [12, 'oneteam', ["Apsa",22,"Alappzha"],134]
My_list.append("Abhiram")
print(My_list)

# Extend

My_list.extend("Abhiram")
print(My_list)

#insert
My_list.insert(1,"Kochi") #inserting an element into a specific location and all other where relocated to the next position
print(My_list)

#clear
My_list.clear() #forclearing all the elements from the list
print(My_list)

#count
list2 = [1,2,4,6,7,3,2,4,2]
print(list2.count(2)) #find the frequency of the number in the list  

# index
print(list2.index(2))
# give only the first index of the given number in the list


#pop

list2.pop()
print(list2)#remove the last element from the list

list2.pop(3)#remove element from the specified location
print(list2)


#remove

list2.remove(4)
print(list2)

#reverse

list2.reverse() #reversing the elemets in the list
print(list2)

#sort

a = [1,4,6,3,8]
a.sort()
print(a)



