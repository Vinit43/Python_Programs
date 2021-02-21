
'''
Write a program which accept one number and display below pattern.
Input : 5

Output : 1
 1 2
 1 2 3
 1 2 3 4
 1 2 3 4 5 
'''

def Pattern(no):
	
	no2=no

	for i in range(0,no,1):
		no3=1
		for j in range(0,no2,1):
			if i>=j:
				print(no3,"\t",end="")
				no3=no3+1
		print()
	
def main():
	value=int(input("Enter the number"))
	Pattern(value)

if __name__ == "__main__":
	main()