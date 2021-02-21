'''
 Write a program which accept one number and display below pattern.
Input : 5
Output : * * * * *
		 * * * *
 		 * * *
 		 * *
 		 * 

'''

def Pattern(no):
	
	no2=no

	for i in range(0,no,1):
		for j in range(0,no2,1):
			if i+j <no:
				print("*\t",end="")
		print()
	
def main():
	value=int(input("Enter the number"))
	Pattern(value)

if __name__ == "__main__":
	main()