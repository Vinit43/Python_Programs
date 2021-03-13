def Sub(no1 , no2):
	return no1 - no2

def SubDecorator(function):

	return function(20 , 25)


def main():

	
	ret=SubDecorator(Sub)
	print("Substraction is :",ret)

if __name__ == '__main__':
	main() 