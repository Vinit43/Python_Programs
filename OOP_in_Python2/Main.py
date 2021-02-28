
class Demo:

	
	def __init__(self , no):

		self.size = no
		self.Arr = []

	def __del__(self):

		print("Deallocating the memory")

		del self.Arr

	def Accept(self):

		print("Enter the N numbers")
		
		for i in range(self.size):
			self.Arr.append(int(input()))

	def Display(self):

		print("The N numbers are")

		for i in range(self.size):
			print(self.Arr[i])

	def Summation(self):
		sum=0
		for i in range(self.size):
			sum=sum+self.Arr[i]
		return sum

	def EvenNumber(self):

		print("The even numbers are:")

		for i in range(self.size):

			if self.Arr[i] % 2 == 0:
				print(self.Arr[i])

	def PerfectNumber(self):

		sum=0

		print("The perfect numbers from the list are:")

		for i in range(self.size):

			for j in range(1,int((self.Arr[i]/2) +1),1):

				if self.Arr[i] % j ==0:
					sum=sum +j

			if sum==self.Arr[i]:
				print(self.Arr[i])
			sum=0


	def PrimeNumber(self):
		
		count = False

		print("Prime Number are :")

		for i in range(self.size):
			
			for j in range(2,(int(self.Arr[i]/2) + 1),1):

				if self.Arr[i] % j ==0:
					count = True
					break
		
			if count == False:
				print(self.Arr[i])

			count = False


def main():
	
	N = int(input("Enter the value of N number\n"))

	obj1 = Demo(N)
	obj1.Accept()
	obj1.Display()
	
	ret = obj1.Summation()
	print("The addition is",ret)

	obj1.EvenNumber()
	obj1.PerfectNumber()
	obj1.PrimeNumber()






'''	
	obj2 = Demo(Arr)

	ret = obj1.EvenNumber()
	print("The even numbers from the list are",ret)

	ret = obj2.OddNumber()
	print("The odd numbers from the list are",ret)
'''

if __name__ == '__main__':
	main()