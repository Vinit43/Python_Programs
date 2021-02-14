def Function(List):
	sum=0
	for i in range(len(List)):
		sum=sum+List[i]

	return sum

def main():

	Arr=[10,20,30]
	
	print("List is:",Arr)

	ret=Function(Arr)

	print("\nSum of N numbers is :",ret)

if __name__ == "__main__":
	main()	