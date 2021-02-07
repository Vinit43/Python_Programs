
#Function accepts nothing and return nothing
def fun():
	print("\nFunction fun")

#Function with parameters
def gun(no):
	print("\nFunction gun",no)

#Function with parameters also with return value
def sun(no):
	print("\nFunction sun with parameter",no)
	return no+1

#Function with parameters and multiple return value
def AddSub(no1,no2):
	add = no1 + no2
	sub = no1 - no2
	return add,sub	

#Entry Function
def main():
	fun()
	gun(11)
	ret=sun(10)
	print("Returned value is:",ret)

	ret1,ret2=AddSub(12,11)
	print("Addition is:",ret1)
	print("Sub is:",ret2)


if __name__ == "__main__":
	main()