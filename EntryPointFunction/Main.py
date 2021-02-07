def Addition(Value1 , Value2):
	Ret = Value1 + Value2
	return Ret


def main():

	No1 = int(input("Enter the number one\n"))                             

	No2 = int(input("Enter the number two\n"))                            

	Ans  = Addition(No1 , No2)

	print("Addition of 2 numbers is :",Ans)

#print(__name__)    # Special Variable

if __name__ == "__main__":    # If module name is main then the flows go to tha Main function in Python
	main()