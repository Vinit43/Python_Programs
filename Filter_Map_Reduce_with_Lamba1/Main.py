# Accept N numbers from user and filter out only even number from that N number
# after that add 2 in every even number
# after that perform summation of all that modified number

#Input : 1 2 3 4 5 
#Ouput: 10
import functools

CheckEven = lambda no: (no%2==0)
Increment = lambda no: no+2
Addition = lambda no1,no2:no1+no2


def main():

	List=[]
	N = int(input("Enter the value of N \n"))
	
	print("Enter the N numbers")
	for i in range(0,N,1):
		value=int(input())
		List.append(value)
		

	print("The entered N numbers are:",List)


	ret=list(filter(CheckEven,List))     #ret=Filterr(List)

	print("The filtered list is:",ret)

	
	ret1=list(map(Increment,ret))    #ret1=Map(ret)

	print("The mapped list is:",ret1)

	ret2=functools.reduce(Addition,ret1)		#ret2=Reduce(ret1) need to import a specific module for Python3

	print("The reduced output is:",ret2)



if __name__ == "__main__":
	main()

# name = lambda parameters:body