
class Base:

	def __init__(self):
		
		self.i =10
		self.j =20
		print("Inside base constructor")

	def Fun(self):

		print("Inside base Fun")

	def Gun(self):

		print("Inside base Gun")

class Derived(Base):

	def __init__(self):
		
		Base.__init__(self)	
		self.x =30
		self.y =40
		print("Inside Derived constructor")

	def Sun(self):

		print("Inside Derived Sun")

	def Gun(self):

		print("Inside Derived Gun")



def main():

	bobj = Base()

	print(bobj.i)
	print(bobj.j)

	bobj.Fun()
	bobj.Gun()


	dobj = Derived()
	print(dobj.i)
	print(dobj.j)
	print(dobj.x)
	print(dobj.y)

	dobj.Sun()
	dobj.Gun()
	dobj.Fun()

if __name__ == '__main__':
	main()