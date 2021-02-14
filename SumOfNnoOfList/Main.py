def Function(List):
	icnt=0
	sum=0

#WHILE LOOP	
	while icnt < len(List):
		sum = sum + List[icnt]
		icnt=icnt+1

	return sum


# FOR LOOP
	#for i in range(len(List)):
	#	sum=sum+List[icnt]

	#return sum

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

	ret=Function(Arr)

	print("\nSum of N numbers is :",ret)

if __name__ == "__main__":
	main()	