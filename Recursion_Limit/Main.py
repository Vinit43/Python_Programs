
import sys

def main():

	print("Reccursive limit",sys.getrecursionlimit())

	sys.setrecursionlimit(1500)
	print("Reccursive limit",sys.getrecursionlimit())
	

if __name__ == "__main__":
	main()	