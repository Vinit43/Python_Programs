i=1     #Defined Variable

def DisplayR():
	global i  # Declared as a Global variable
	print(i)
	i=i+1
	DisplayR()


def main():

	#value=int(input("Enter the number of iteration\n"))
	
	print("Reccursive Way")
	DisplayR()

	

if __name__ == "__main__":
	main()	