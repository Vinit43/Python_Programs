
class Base1:

	def __init__(self):
		
		self.i =10
		self.j =20
		print("Inside base1 constructor")

class Base2:

	def __init__(self):
		
		self.a =100
		self.b =200
		print("Inside base2 constructor")

	
class Derived(Base1,Base2):

	def __init__(self):
		
		Base1.__init__(self)
		Base2.__init__(self)	
		self.x =30
		self.y =40
		print("Inside Derived constructor")



def main():

	dobj = Derived()

	print(dobj.i)
	print(dobj.j)
	print(dobj.a)
	print(dobj.b)
	print(dobj.x)
	print(dobj.y)
	


if __name__ == '__main__':
	main()