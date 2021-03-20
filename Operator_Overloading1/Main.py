
class Student:

	def __init__(self,str,a,b,c):
		self.name=str
		self.m1=a
		self.m2=b
		self.m3=c
	
	def __eq__(self,other):

		if self.m1==other.m1 and self.m2==other.m2 and self.m3==other.m3:
			return True
		else:
			return False

	def __gt__(self,other):

		if self.m1>other.m1 and self.m2>other.m2 and self.m3>other.m3:
			return True
		else:
			return False


def main():

	obj1 =Student("Vinit",100,100,100)
	obj2=Student("Nandurkar",90,80,70)

	if obj1==obj2:
		print("Marks of Students are same")
	else:
		print("Marks are different")

	if obj1>obj2:
		print("Marks of Student 1 are more than Student 2")
	else:
		print("Marks of Student 1 are less than Student 2")



if __name__ == '__main__':
	main(),