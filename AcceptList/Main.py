def main():

	Arr=[]
	
	print("Enter the size of the List")
	size=int(input())

	print("Enter the elements in the Lis")

	for i in range(size):
		value=int(input())
		Arr.append(value)

	print("The accepted List is ",Arr)

if __name__ == "__main__":
	main()	