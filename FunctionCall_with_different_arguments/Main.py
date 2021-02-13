
# Function with Positional Arguments

def Student(Name ,Roll_no,Address,Age):
	print("\nStudent Funtion\n")
	print("Name is:",Name)
	print("Roll_no is:",Roll_no)
	print("Address is:",Address)
	print("Age is:",Age)


# Function with Keyword Arguments

def Computer(Ram , Processor , HDD):
	print("\nComputer Function\n")
	print("Ram size is:",Ram)
	print("Processor is:",Processor)
	print("HDD is:",HDD)

# Function with Default Arguments

def CricleArea(Radius , Pi=3.14):
	print()
	return Pi * Radius * Radius

# Variable Number of arguments

def Fun(*Value):
	print("\nNumber of arguments are:",len(Value))


def main():
	
	Student("Vinit",129,"Pune",22)

	Computer(Processor="i9",Ram="16GB",HDD="2TB")

	ret=CricleArea(10)    #Will consider the default value
	print("Area of Cricle is:",ret)

	ret=CricleArea(10,2)  #Will over write the default value
	print("Area of Cricle is:",ret)

	Fun(10,20,30)
	Fun(10)
	Fun()


if __name__ == "__main__":
	main()