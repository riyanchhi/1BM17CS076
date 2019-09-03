#(lab)4.a university want to approve their admission..........


import sys
class Student:
	def __init__(self):
		self.studentId=None
		self.age=None
		self.marks=None
	def setter(self):
		self.studentId=input("Enter the id:")
		self.age=int(input("Enter the age:"))
		self.marks=int(input("Enter the marks:"))		
	def getter(self):
		print("----------STUDENT DETAILS-----------------")		
		print("Student Id:",self.studentId,"\nStudent Age:",self.age,"\nStudent mark:",self.marks)
	def validate_marks(self):
		if self.marks<=100 and self.marks>0:
			return True
		else:
			return False
	def validate_age(self):
		if self.age>20:
			return True
		else:
			return False
	def check_qualification(self):
		if self.validate_marks() and self.validate_age():
			if self.marks>64:
				return True
			else:
				return False
		else:
			return False
s1=Student()
s1.setter()
s1.getter()
if s1.check_qualification():
	print("Student admission aproved")
else:
	print("Student admission disproved")	
