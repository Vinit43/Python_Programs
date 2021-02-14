import Vinit

def main():

	value = int(input("Enter the number\n"))
	ret=Vinit.CheckEven(value)

	if ret==True:
		print("Number is even")
	else:
		print("Number is odd")

if __name__ == "__main__":
	main()
