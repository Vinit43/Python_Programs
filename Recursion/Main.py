def DisplayI(no):

	for i in range(no):
		print("BYE")

def DisplayR(no):

	if no==0:
		return
	else:
		#no=no-1
		print("Hello")
		DisplayR(no-1)


def main():

	value=int(input("Enter the number of iteration\n"))
	print("Iterative Way")
	DisplayI(value)

	print("Reccursive Way")
	DisplayR(value)

	

if __name__ == "__main__":
	main()	