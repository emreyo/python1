# emreyo 
class student:
	def __init__(self):
		self.name = raw_input("Enter name: ")
		self.surname = raw_input("Enter surname: ")
		self.stdNum = raw_input("Enter student number: ")
		self.classNum = raw_input("Enter class number: ")
		self.cGpa = raw_input("Enter CGPA: ")
		
	def writeStudent(self): #
		print "Student name: ", self.name
		print "Student surname: ", self.surname
		print "Student number: ", self.stdNum
		print "Student class number: ", self.classNum
		print "Student CGPA: ", self.cGpa