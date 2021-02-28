
class Demo:

	x=10
	y=20

	def __init__(self):
		print("inside special function")

		self.i = 30
		self.j = 40

	def __del__(self):
		print("Inside destructor like function")   

	def fun(self):
		print("Inside function")

def main():
	
	obj1 = Demo()
	obj2 = Demo()

	obj1.fun()
	obj2.fun()

	del obj1    # to explicitly call the delete (destructor) It by default gets called with__del__
	del obj2
	

if __name__ == '__main__':
	main()