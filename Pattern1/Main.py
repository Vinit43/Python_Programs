# Write a program which accept one number and display below pattern.
#Input : 5
#Output :
 # 	* * * * *
 # 	* * * * *
 # 	* * * * *
 # 	* * * * *
 # 	* * * * * 

def Pattern(no):

	no2 = no
	for i in range(0,no,1):
		for j in range(0,no2,1):
			print("*\t",end="")
		print()


def main():

	value=int(input("\nEnter the number:\n"))
	Pattern(value)

if __name__ == "__main__":
	main()