class Base:

	def __init__(self):

		self.no1 = 11    #public
		self._no2 = 21   #protected
		self.__no3 = 31  #private

	def fun(self):                                    # Public Method
		print(self.no1 , self._no2,self.__no3)

	def _fun(self):                                   # Protected Method
		print(self.no1 , self._no2,self.__no3)

	def __fun(self):								 # Private Method
		print(self.no1 , self._no2,self.__no3)

class Derived(Base):
	
	def __init__(self):
		Base.__init__(self)

	def gun(self):

		print(self.no1)
		print(self._no2)
		#print(self.__no3)           NA

		self.fun()
		self._fun()
		#self.__fun()               NA


def main():

	bobj = Base()

	print(bobj.no1)
	print(bobj._no2)
	#print(bobj.__no3)      NA
	bobj.fun()
	bobj._fun()
	#bobj.__fun()          NA
	

	dobj = Derived()

	dobj.gun()

if __name__ == "__main__":
	main()