
i=0
add=0

def Addition(arr):
	global i
	global add
	if i != len(arr):
		add = add+arr[i]
		i=i+1
		Addition(arr)
	return add

def main():

	Arr=[]
	icnt=0

	print("Enter the N number")
	no=int(input())

	print("Enter the elements")

	for icnt in range(0,no):
		print("Enter the element number :",icnt+1)
		value=int(input())
		Arr.append(value)

	print("List is:",Arr)

	ret=Addition(Arr)

	print("\nSum of N numbers by recursive is :",ret)


if __name__ == "__main__":
	main()	