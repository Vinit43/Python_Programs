import os
import threading
from time import sleep

def Thread1(no):

	print("Thread1 is created")
	print("PID of Thread1 is ",os.getpid())
	for i in range(no):
		sleep(1)
		print("Thread1",i)
	
def Thread2(no):

	print("Thread2 is created")
	print("PID of Thread2 is ",os.getpid())
	for i in range(no):
		sleep(1)
		print("Thread2",i)
	
def main():

	print("Inside main thread")
	print("PID of main thread is ",os.getpid())
	print("PID of parent thread of main is ",os.getppid())
	print()

	value=10

	t1 = threading.Thread(target = Thread1 , args=(value,))
	t2 = threading.Thread(target = Thread2 , args=(value,))

	t1.start()
	t2.start()

	print("End of main process")

if __name__ == "__main__":
	main()