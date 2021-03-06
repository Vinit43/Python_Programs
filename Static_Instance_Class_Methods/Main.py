



	# Instance method should be called using Objects and class method should be called by class name
	# If method is related with instance variables then define Instance method
	# If method is related with class variable then define Class method
	# We use decorator for accepting the "cls" parameter for the class method




class Student:

	School = "Teresa"

	def __init__(self , no1 ,no2 ,no3):
		
		self.m1 = no1
		self.m2 = no2
		self.m3 = no3

	def InstanceTotal(self):
		
		return self.m1 +self.m2+self.m3

	@classmethod                       #Decorator
	def Class_DisplaySchool(cls):

		print("School name is:",cls.School)

	@staticmethod
	def Static_Info():

		print("This function shows info abt School")


def main():

	Student.Class_DisplaySchool()
	obj1 = Student(50,80,70)
	obj2 = Student(60,70,80)
	ret = obj1.InstanceTotal()
	print("Total marks are:",ret)
	Student.Static_Info()


if __name__ == '__main__':
	main()