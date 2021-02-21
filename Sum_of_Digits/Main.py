def DigitAdd(no):
	
	add=0
	digit=0

	while no!=0:

		digit=int(no%10)
		add=add+digit
		no=int(no/10)
	return add

	
def main():

	value = int(input("Enter the string\n"))
	ret=DigitAdd(value)
	print("Addition of the digits is:",ret)

if __name__ == "__main__":
	main()