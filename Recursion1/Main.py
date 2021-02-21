
def DisplayR():

	i=1
	print(i)
	i=i+1
	DisplayR()


def main():

	#value=int(input("Enter the number of iteration\n"))
	
	print("Reccursive Way")
	DisplayR()

	

if __name__ == "__main__":
	main()	