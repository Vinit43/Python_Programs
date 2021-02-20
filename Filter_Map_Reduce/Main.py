# Accept N numbers from user and filter out only even number from that N number
# after that add 2 in every even number
# after that perform summation of all that modified number

#Input : 1 2 3 4 5 
#Ouput: 10
def Reduce(crr):
	sum=0
	for i in range(len(crr)):
		sum=crr[i]+sum
	return sum

def Map(brr):
	crr=[]
	for i in range(len(brr)):
		no=brr[i]+2
		crr.append(no)
	return crr

def CheckEven(no):

	if no%2==0:
		return True
	else:
		return False

	#for i in range(0,len(List),1)

def Filterr(arr):
	brr=[]

	for i in range(0,len(arr),1):
		if CheckEven(arr[i])==True:
			brr.append(arr[i])
	return brr


def main():

	List=[]
	N = int(input("Enter the value of N \n"))
	
	print("Enter the N numbers")
	for i in range(0,N,1):
		value=int(input())
		List.append(value)
		CheckEven(value)

	print("The entered N numbers are:",List)

	ret=Filterr(List)

	print("The filtered list is:",ret)

	ret1=Map(ret)

	print("The mapped list is:",ret1)

	ret2=Reduce(ret1)

	print("The reduced output is:",ret2)



if __name__ == "__main__":
	main()

# name = lambda parameters:body