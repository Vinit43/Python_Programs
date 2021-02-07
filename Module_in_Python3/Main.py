import Vinit

def main():

	value1=int(input("Enter the number 1\n"))
	value2=int(input("Enter the number 2\n"))
	ret1=Vinit.Addition(value1,value2)
	print("Addition is:",ret1)
	print()

	value1=int(input("Enter the number 1\n"))
	value2=int(input("Enter the number 2\n"))
	ret2=Vinit.Subtraction(value1,value2)
	print("Subtraction is:",ret2)
	print()

#Code starter
if __name__ == '__main__':
	main()
	
