student_id = 1
borrowed_book = {}


library =["python for beginners", "data structures in C", "AI basics"]

def start():
	while True:
		print("1. display all books\n2. add book\n3. borrow book\n4. return book\n5. borrowed books\n6. students that borrowed books\n7. exit")
		user_choice = int(input("enter an option to continue: "))
		call_function(user_choice)

def call_function(user_choice):
	if user_choice == 1:
		display_books()

	elif user_choice == 2:
		book_name = input("enter the name of the book to add: ")
		add_book(book_name)

	elif user_choice == 3:
		book_name = input("enter a book name to borrow: ")
		borrow_book(book_name)

	elif user_choice == 4:
		book_name = input("enter a book name to return: ")
		book_return(book_name)

	elif user_choice == 5:
		borrowed(borrowed)

	elif user_choice == 6:
		student_that_borrowed(student_that_borrowed)

	elif user_choice == 7:
		print("termination success")
		exit()
	else:
		print("out of range")		

def display_books():
	if len(library) != 0:
		for book in library:
			print(book)	
								
	else:
		print("no book in library")

def add_book(book_name):
	if book_name in library:
		print("book already exist")
				
	else:
		library.append(book_name)
			
def borrow_book(book_name):
	if book_name in library:
		global student_id
		borrowed_book[student_id] = book_name
		library.remove(book_name)
		student_id += 1
	else:
		print("book not available")	

def book_return(book_name):
	for book in borrowed_book:
		if book_name == borrowed_book[book]:
			print("book returned successfully")
		#	borrowed_book.pop(book)
			library.append(book_name)
	else:
		print("book not found in your borrowed list")	

def borrowed(borrowed):
	print(borrowed_book)

def student_that_borrowed(student_that_borrowed):
	for student in borrowed_book:
		if len(borrowed_book) != 0:
			print(student)
	else: 
		print("no student borrowed a book")		
	

start()










