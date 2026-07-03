#Add Student Details
students = []
def add_student():
	student_id = int(input("Enter the Student Id:"))
	student_name = input("Enter the Student name:")
	student_mark = float(input("Enter the Student Mark:"))
	student = {"id": student_id,"Name":student_name,"Mark":student_mark}
	students.append(student)

#View student
def view_student():
	if(len(students) == 0):
		print("No student detais!")
		return
	else:
		print("\nStudent Records")
		print("-"*40)
		for i in students:
			print("ID =",i["id"],end = "|")
			print("Name =",i["Name"],end ="|")
			print("Mark = ",i["Mark"])
			print("-"*40)

#search student()
def search_student():
	search_id = int(input("Enter the search Id:"))
	for j in students:
		if search_id == j["id"]:
			print("\n==Student Details==")
			print("ID =",j["id"],end = "|")
			print("Name =",j["Name"],end ="|")
			print("Mark = ",j["Mark"])
			return
	print("Student not found!")

# average score of the students
def average_score():
	if(len(students) == 0):
		print("No student detais!")
		return
	sum = 0
	for k in students:
		sum += k["Mark"]
	avg = sum / len(students)
	print("Average Score :",avg)
	
#Sort student by  Mark
def sort():
	if(len(students) == 0):
		print("No student details!")
		return
	students.sort(key=lambda x: x["Mark"])
	print("Students sorted by Student Mark.\n")
	view_student()

	
	
		
#Menu Driven
while True:
	print("\n========Student Management System========\n1. Add a Student Details\n2.View Student Record\n3.Search a student details\n4.Get average score of students\n5.Sort students by mark\n6.Exit\n ")
	choose = int(input("Choose anyone:"))
	if choose == 1:
		add_student()
		
	elif choose == 2:
		view_student()
		
	elif choose == 3:
		search_student()
		
	elif choose == 4:
		average_score()
		
	elif choose == 5:
		sort()
		
	elif choose == 6:
		print("Thank you...")
		break
	else:
		print("Invalid Input")
