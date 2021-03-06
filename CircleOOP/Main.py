
class Circle:

	def __init__(self):

		self.radius = 0.0
		self.circumference = 0.0
		self.area = 0.0
	
	def Accept(self):

		self.radius = float(input("Enter the value of radius\n"))

	def CircleArea(self):

		self.area = 3.14 * self.radius * self.radius

	def CircleCircumference(self):

		self.circumference = 2 * 3.14 * self.radius

	def Display(self):

		print("Radius of Circle is :", self.radius)
		print("Area of Circle is :", self.area)
		print("Circumference of Circle is:",self.circumference)


def main():

	obj = Circle()

	obj.Accept()
	obj.CircleArea()
	obj.CircleCircumference()
	obj.Display()

if __name__ == "__main__":
	main()