#This program is known as MUTEX

import threading
import os

Amount = 1000

def ATM(func ,lock):
	func(lock)

def Deposit(lock):

	lock.acquire()

	value=int(input("Enter the amount to Deposit\n"))

	global Amount

	Amount = Amount + value
	print("Dposit successful\nBalance-:",Amount)
	
	lock.release()

def WithDraw(lock):


	lock.acquire()

	value=int(input("Enter the amount to withdraw\n"))
	global Amount

	if value>Amount:
		print("Insufficient Balance")
	else:
		
		Amount = Amount - value
		print("withdraw successful\nBalance-:",Amount)
	
	lock.release()

def main():

	print("Inside main")

	lock = threading.Lock()

	t1 = threading.Thread( target = ATM , args = (Deposit , lock,))
	t2 = threading.Thread( target = ATM , args = (WithDraw , lock,))

	t1.start()
	t2.start()
	t1.join()
	t2.join()

	print("ATM application closed")

if __name__ == "__main__":
	main()