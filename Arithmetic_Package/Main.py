import Arithmetic

def main():

	value1=int(input("Enter the first number"))
	value2=int(input("Enter the second number"))

	ret=Arithmetic.Add(value1,value2)
	print("Addition is:",ret)

	ret=Arithmetic.Sub(value1,value2)
	print("Substraction is:",ret)

	ret=Arithmetic.Mul(value1,value2)
	print("Multiplication is:",ret)

	ret=Arithmetic.Div(value1,value2)
	print("Division is:",ret)

if __name__ == "__main__":
	main()