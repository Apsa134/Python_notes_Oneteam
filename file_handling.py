# f= open("text.txt","w") # for opening the file
# f.write("Hi am apsa,you are....")

# f.close()


#with

with open("text.txt","r") as fp:
	# fp.write("\n am appended!!!")
	# print(fp.read())  for getting the contemts in the file
	# print(fp.readline()) #for getting the contents in the file line by line
	print(fp.readlines()) #for getting all the contents in the file in a list