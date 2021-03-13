def Substraction(no1 , no2):
	return no1 - no2

def SubDecorator(function):

	def Updater(a,b):

		if a < b :
			a,b = b,a
	
		return function(a,b)


	return Updater


def main():

	sub = SubDecorator(Substraction)
	x=int(input("Enter 1st number:\n"))
	y=int(input("Enter 2nd number:\n"))
	
	ret = sub(x,y)

	print("Substraction is :",ret)

if __name__ == '__main__':
	main() 