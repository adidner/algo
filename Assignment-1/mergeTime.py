import re
from time import time
import random

def merge_sort(list_ints):
	if len(list_ints)==1:
		return list_ints
	else:
		sorted_half_1 = merge_sort(list_ints[:len(list_ints)//2])
		sorted_half_2 = merge_sort(list_ints[len(list_ints)//2:])
		return merge(sorted_half_1, sorted_half_2)


def merge(half_1, half_2):
	counter_1 = 0
	counter_2 = 0
	new_list = []
	while counter_1 < len(half_1) or counter_2 < len(half_2):
		
		if counter_1 > len(half_1)-1:
			new_list.append(half_2[counter_2])
			counter_2+=1
			
		elif counter_2 > len(half_2)-1:
			new_list.append(half_1[counter_1])
			counter_1+=1

		else:
			if half_1[counter_1] < half_2[counter_2]:
				#print("first")
				new_list.append(half_1[counter_1])
				counter_1+=1
			elif half_1[counter_1] >= half_2[counter_2]:
				#print("second")
				new_list.append(half_2[counter_2])
				counter_2+=1
	return new_list

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
		
		sorted = merge_sort(unsorted)
		
		end = time()
		
		difference = end - begin
		print(" time: "+ str(round(difference, 6))+" , "+"n: "+ str(x))
	
	
main()