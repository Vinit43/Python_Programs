
class Airthmetic:                              #Class Definition

	def __init__(self , i , j):               # Constructor known as special function in Python

		self.no1 = i                          # Class instance variable

		self.no2 = j                          # class instance varible

	def Add(self):                            # Instance Method
		return self.no1 + self.no2

	def Sub(self):                            # Instance Method
		return self.no1 - self.no2
		



def main():

	obj1= Airthmetic(11,21)           #  __init__(obj1 , 11 ,21)
	obj2= Airthmetic(101,51)
	
	ret = obj1.Add()                  # Add(obj1)
	print("Addition is:",ret)

	ret = obj1.Sub()                  
	print("Substraction is:",ret)

	ret = obj2.Add()                  # Add(obj2)
	print("Addition is:",ret)

	ret = obj2.Sub()                  
	print("Substraction is:",ret)
	
	
if __name__ == '__main__':
	main()