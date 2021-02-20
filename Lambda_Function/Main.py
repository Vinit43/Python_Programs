
# Named function

def Additon(no1,no2):
	return no1+no2

# Lambda function

Sum = lambda no1,no2 : no1+no2 

def fun(name):
	ret=name(10,40)
	print("Additon is:",ret)

def main():

	value1=int(input("Enter first number\n"))
	value2=int(input("Enter second number\n"))
	ret=Additon(value1,value2)
	print("Addition is :",ret)

	ret = Sum(value1,value2)
	print("Sum is :",ret)

	fun(Sum)
if __name__ == "__main__":
	main()

# name = lambda parameters:body