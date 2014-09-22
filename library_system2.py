from  library_system1 import *

#db = MySQLdb.connect("localhost","root","1CLOUD","Librarysystem_project" )
#cursor = db.cursor()


print "//**********************************//"
print "    LIBRARY MANGAGEMENT SYSTEM   "
print  "//**********************************//"

s1 = student()
b1 = book()

while True:
		print "\n1.Admin\n2.Student\n3.Exit"
		n=raw_input("Enter your choice:")
		if n == '1':
				print "ADMIN MENU"
				admin = raw_input("enter username:")
				password = raw_input("\nenter password:")
				if admin!='Admin' or password!='Admin':
   	    				print "Unauthorised Access!"
       					exit()
	
				else:
			 			while True:
	   							print "\nAdmin Particulars\n1.Display Student list\n2.View Book Details\n3.Delete Student Record\n4.Add Books\n5.Exit\n"
 	 							m=raw_input("enter your choice:")
 	  							if m == '1':
 			 							s1.Display_studentlist()
 			 							numrows = int (cursor.rowcount)
										for x in range(0, numrows):
											row = cursor.fetchone()
											print row[0],"-->",row [1],"-->",row[2],"-->",row[3]
										 
 			 							
 			 					elif m =='2':
 			 							b1.Display_Books()
 			 							numrows = int (cursor.rowcount)
										for x in range(0, numrows):
											row = cursor.fetchone()
											print row[0],"-->",row [1],"-->",row[2]
										
			 					elif m =='3':
 										j = input('enter usn of student to be removed:')
 										
 										

  								elif m =='4':
  									   	b1.create_book()
  									   	

  								else:
  								    	break	    


		elif n =='2': 			     	    	
	    		print "***Student MENU***"
	    		s1.Student_details()
	    		s1.add_student()
	    		
 	     	     	
 		else:
 				db.close()
 				exit()   	


