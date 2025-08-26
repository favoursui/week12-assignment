student_db = {}
#function to start our program

def start():
	while True:
		print("1. add student \n2. delete student\n3. update student record\n4. get student record\n5. display all students\n6. search student\n7. count students\n8. age filter")
		user_choice = int(input("select an option to proceed: "))
		if user_choice == 1:
			add_student()
			print("i am back to the start function")

		elif user_choice == 2:
			delete_student()

		elif user_choice == 3:
			student_update()

		elif user_choice == 4:
			a_student()	
		
		elif user_choice == 5:
			all_student()

		elif user_choice == 6:
			name_search()

		elif user_choice == 7:
			student_count()		

		elif user_choice == 8:
			age_filter()	

		else:
			print("input out of range")

def add_student():
	print("i am executing add student logic")
	name = input("student name: ")
	age = int(input("student age: "))
	department = input("department: ")
	key = len(student_db) + 1
	student_db[key] = {"name": name,
			   "age": age,
			   "dept": department
			   }
	print(student_db)

def delete_student():
	student_id = int(input("student id to delete: "))	
	if student_id in student_db:
		del student_db[student_id]
		print(f"student with id {student_id} deleted successfully!")
		print(student_db)
	else:
		print(f"student with ID {student_id} not found")	

def student_update():
	id_update = int(input("enter id u want to update: "))	
	if id_update in student_db:
		print("1. name\n2. age\n3. department")
		option = int(input("select an option to update: "))
		if option == 1:
			name_update = input("enter new name for student: ")
			student_db[id_update]["name"] = name_update
			print(student_db)

		elif option == 2:
			age_update = int(input("enter the new age: "))
			student_db[id_update]["age"] = age_update
			print(student_db)

		elif option == 3:
			dep_update = input("enter new department: ")
			student_db[id_update]["department"] = dep_update
			print(student_db)	
	else:
		print(f"student with ID {id_update} not found")

def a_student():
	a_student = int(input("enter a student id to get a student: "))
	if a_student in student_db:
		print("name:", student_db[a_student]["name"])
		print("age:", student_db[a_student]["age"])
		print("department:", student_db[a_student]["dept"])
	
	else:
		print(f"student with ID {a_student} not found")	

def all_student():
	for student in student_db:
		print("name:", student_db[student]["name"])
		print("age:", student_db[student]["age"])
		print("department:", student_db[student]["dept"])

def name_search():
	student_name = input("enter a students name to search: ")
	for i in student_db:
		if i in student_db and student_name == student_db[i]["name"]:	
			print(student_db[i])	

	else:
		print(f"student with name {student_name} does not exist")

def student_count():
	count = 0
	for student in student_db:
		if count < len(student_db):
			count += 1
	print(f"found a total of {count} students")
		
def age_filter():
	count = 0
	age = int(input("enter an age for your filter: "))
	for student in student_db:
		if student_db[student]["age"] >= age and count < len(student_db):
			count += 1
			print(student_db[student])


start()





























