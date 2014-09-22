import MySQLdb

db = MySQLdb.connect("localhost","root","1CLOUD","Librarysystem_project" )
cursor = db.cursor()

studentdetails_list = [ ]
class student ():

	def Student_details(self):
		print " Please enter your curiculum details below\n"
		b=raw_input("Enter your name :")
		print ("your name is " +b)
		a=raw_input("Enter your USN :")
		print ("Your USN is",int(a))
		c=raw_input("Enter your branch :")		
		print ("your  baranch is " +c)
		d=raw_input("Enter your current semester :")
		print ("you are in the semester",int(d))
		studentdetails_list.extend((a,b,c,d))

	def add_student(studentdetails_list):
		sql1 = """INSERT INTO Students_list(USN,Student_name,Branch,Sem )VALUES (studentdetails_list)"""
		cursor.execute(sql1)
		db.commit()

	def  Display_studentlist(self):
		sql1 = """SELECT *FROM	Students_list """
		cursor.execute(sql1)
		db.commit()
		
bookdetails_list = [ ]
class book ():
	
	def create_book(self):
		number = input("enter Bookno:")
		book_name = raw_input("enter Book_name:")
		author_name = raw_input("enter author_name:")
		bookdetails_list.extend((number,book_name,author_name))
		try:
				sql="""INSERT INTO Booklist(Bookno,Bookname,Authorname) VALUES (bookdetails_list)"""
				cursor.execute(sql)
				db.commit()
		except:
				db.rollback()


				
	def Display_Books(self):
		sql1 = """SELECT *FROM Booklist """ 
		cursor.execute(sql1)
		db.commit()
		
