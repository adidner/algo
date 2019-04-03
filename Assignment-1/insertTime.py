import re
from time import time
import random

def sort(list):
	for x in range(0,len(list)):
		#print(list)
		for i in range(x,-1,-1):
			#if I am the first element
			if x == 0:
				#print("first")
				continue
			#if I am greater than the left element
			if list[x] >= list[x-1]:
				#print("greater than left: "+ str(list[x]) + ", "+ str(list[x-1]))
				continue
			#if There is no left element
			if i == 0:
				#print("i of 0")
				#print(list)
				temp=list[x]
				del list[x]
				list.insert(0,temp)
				continue
				
			
			#if I am between 2 elements
			if i-1 >= 0:
				if list[i-1] < list[x] and list[x] <= list[i]:
						#print("in 2 between")
						#print(list)
						temp = list[x]
						del list[x]
						list.insert(i,temp)
						continue
						
						
	return list
	
	
	
def generate(amount):
	initiallist = []
	for x in range(0,amount):
		initiallist.append(random.randint(1,10001))
	return initiallist
	
def main():
	print("this program will randomly generate n numbers between 0 and 10,000 to be sorted via this algorithm while keeping track of the amount of time taken for that.\n")
	print("Note: the time to generate the huge arrays isn't factored into the sorting time")
	list_of_n = [100, 1000, 1500, 2500, 5000, 7500, 10000, 12500, 15000, 20000 ]
	
	for x in list_of_n:
		
		unsorted = generate(x)
		
		begin = time()
		
		sorted = sort(unsorted)
		
		end = time()
		
		difference = end - begin
		print(" time: "+ str(difference)+" , "+"n: "+ str(x))
		
	
	
main()