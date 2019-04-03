import re
from time import time
import random

#this function runs and insertion sort on the data,
def sort(list):
	for x in range(0,len(list)):#through all element
		
		for i in range(x,-1,-1): #backwards through sorted elements
			#if I am the first element, I'm arbitrarily sorted
			if x == 0:
				continue
			
			#if I am greater than the left element, I'm arbitrarily sorted
			if list[x] >= list[x-1]:
				continue
			
			#if There is no left element, I belong at the head of the list
			if i == 0:
				temp=list[x]
				del list[x]
				list.insert(0,temp)
				continue
				
			
			#if I am between 2 elements, I belong in between
			if i-1 >= 0:
				if list[i-1] < list[x] and list[x] <= list[i]:
						temp = list[x]
						del list[x]
						list.insert(i,temp)
						continue
						
						
	return list
	
	
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
	
	
	list_of_n = [100, 1000, 1500, 2500, 5000, 7500, 10000, 12500, 15000, 20000 ]
	
	for x in list_of_n:
		
		unsorted = generate(x)
		
		begin = time()
		
		sorted = sort(unsorted)
		
		end = time()
		
		difference = end - begin
		print(" time: "+ str(round(difference, 6))+" , "+"n: "+ str(x))
		
	
	
main()