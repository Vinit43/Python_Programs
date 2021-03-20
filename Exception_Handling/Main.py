

def main():
	
	no1 = int(input("Enter the value\n"))
	no2 = int(input("Enter the value\n"))

	try:
		ans=no1/no2

	except Exception as eobj:
		print("Exception occurs:",eobj)
		print("Use second number other than 0")
	else:
		print("Division is:",ans)


if __name__ == '__main__':
	main()