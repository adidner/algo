import re
from time import time
import random
import math

def stooge_sort(list_ints):
	
	if len(list_ints) == 2 and list_ints[0] > list_ints[1]:
		temp = list_ints[0]
		list_ints[0] = list_ints[1]
		list_ints[1] = temp
	elif len(list_ints) > 2:
		twothirds = int(math.ceil(len(list_ints) * 2 / 3))
		list_ints[:twothirds] = stooge_sort(list_ints[:twothirds])
		list_ints[(len(list_ints)-twothirds):] = stooge_sort(list_ints[(len(list_ints)-twothirds):])
		list_ints[:twothirds] = stooge_sort(list_ints[:twothirds])
	return list_ints
	
	
#this array generates random integers between 1 and 10000 and returns them into a list
def generate(amount):
	initiallist = []
	for x in range(0,amount):
		initiallist.append(random.randint(1,10001))
	return initiallist
	
	
def main():
	#intro message
	print("this program will randomly generate n numbers between 0 and 10,000 to be sorted via this algorithm while keeping track of the amount of time taken for that.\n")
	print("Note: the time to generate the huge arrays isn't factored into the sorting time")
	list_of_n = [ 50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800]
	
	for x in list_of_n:
		
		unsorted = generate(x)
		
		begin = time()
		
		sorted = stooge_sort(unsorted)
		
		end = time()
		
		difference = end - begin
		print(" time: "+ str(round(difference, 6))+" , "+"n: "+ str(x))
	
	
main()