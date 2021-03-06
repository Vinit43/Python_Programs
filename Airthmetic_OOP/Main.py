
class Arithmetic:

	def __init__(self):

		self.value1 = 0
		self.value2 = 0
	
	
	def Accept(self):

		self.value1 = int(input("Enter the value of 1st number\n"))
		self.value2 = int(input("Enter the value of 2nd number\n"))

	def Addition(self):

		return self.value1 + self.value2

	def Substraction(self):

		return self.value1 - self.value2

	def Multiplication(self):

		return self.value1 * self.value2
	
	def Division(self):

		return self.value1 / self.value2
	

def main():

	obj = Arithmetic()

	obj.Accept()
	ret=obj.Addition()
	print("Addition is:",ret)

	ret=obj.Substraction()
	print("Differnce is:",ret)

	ret=obj.Multiplication()
	print("Multiplication is:",ret)

	ret=obj.Division()
	print("Division is:",ret)
if __name__ == "__main__":
	main()