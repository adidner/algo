import re
import sys
import time
import random

#Next to do
#make the create random bin packing scenarios part
#enter the 20 cases into excel and make charts/graph

#look up problem 2 on wikipedia 
#do a
#do b


class test_case:
	def __init__(self, list_items, bin_capacity):
		list_items.reverse()
		self.list_items = list_items
		self.bin_capacity = bin_capacity
	def printself(self):
		print("Item List: ", end="")
		print(self.list_items)
		print("bin_capacity: ", end="")
		print(self.bin_capacity)



def First_Fit(test_case):
	bins = []
	copy_list_items = test_case.list_items.copy()
	current_item=copy_list_items.pop()
	bins.append(current_item)
	placed = False
	while len(copy_list_items)>0:
		#print(bins)
		current_item=copy_list_items.pop()
		for i in range(0, len(bins)):
			if current_item + bins[i] <= test_case.bin_capacity:
				bins[i] += current_item
				placed = True
				break
		if placed == False:
			bins.append(current_item)
		elif placed == True:
			placed = False
	#print("First Fit: ", end="")
	#print(bins)
	return len(bins)
	
def First_Fit_Dec(test_case):
	bins = []
	
	copy_list_items = test_case.list_items.copy()
	copy_list_items.sort()
	#print("List, Reversed: ", end="")
	#print(copy_list_items)
	current_item=copy_list_items.pop()
	
	bins.append(current_item)
	placed = False
	while len(copy_list_items)>0:
		#print(bins)
		current_item=copy_list_items.pop()
		for i in range(0, len(bins)):
			if current_item + bins[i] <= test_case.bin_capacity:
				bins[i] += current_item
				placed = True
				break
		if placed == False:
			bins.append(current_item)
		elif placed == True:
			placed = False
	#print("First Fit Dec: ", end="")
	#print(bins)
	return len(bins)

def Best_Fit(test_case):
	bins = []
	copy_list_items = test_case.list_items.copy()
	current_item = copy_list_items.pop()
	bins.append(current_item)
	placed = False
	while len(copy_list_items)>0:
		#print(bins)
		current_item=copy_list_items.pop()
		left_over_space = 1000000
		current_index = -1
		for i in range(0, len(bins)):
			if current_item + bins[i] <= test_case.bin_capacity and test_case.bin_capacity - (current_item + bins[i]) < left_over_space :
				
				current_index = i
				left_over_space = test_case.bin_capacity - (current_item + bins[i])
				placed = True
				#print("Current index: "+str(current_index))
				#print("Left Over Space: "+str(left_over_space))
		if placed == False:
			bins.append(current_item)
		elif placed == True:
			bins[current_index]+=current_item
			placed = False
	return len(bins)		
	
	#print("Best Fit: ", end="")
	#print(bins)
	
	
def createtestcases():
	list_of_test_cases = []
	for x in range(0, 25):
		bin_capacity = random.randint(1,101)
		number_items = random.randint(1,101)
		list_items = []
		for i in range(0,number_items):
			item_weight = random.randint(1,bin_capacity)
			list_items.append(item_weight)
		newtest = test_case(list_items, bin_capacity)
		list_of_test_cases.append(newtest)
	return list_of_test_cases
	

def main():
	
	fname = "bin.txt"
	content = []
	list_of_test_cases = []
	multiply_constant = 1000000
	
	#Reading in all test cases from files
	list_of_test_cases = createtestcases()	
	
	for i in range(0,len(list_of_test_cases)):		
		
		
		#run First-fit
		start = time.time()
		bin_len = First_Fit(list_of_test_cases[i])
		end = time.time()
		final=end-start
		final = final * multiply_constant
		final = round(final, 2)
		print("First Fit: "+ str(i))
		print("Time: "+str(final))
		print("Bins: "+ str(bin_len))
		print()
	
	print()
	print()
	
	for i in range(0,len(list_of_test_cases)):
		
		#run First-fit decreasing
		start = time.time()
		bin_len =First_Fit_Dec(list_of_test_cases[i])
		end = time.time()
		final=end-start
		final = final * multiply_constant
		final = round(final, 2)
		print("First Fit Decreasing: "+ str(i))
		print("Time: "+str(final))
		print("Bins: "+ str(bin_len))
		print()
	
	print()
	print()
	
	for i in range(0,len(list_of_test_cases)):
		
		#run Best-fit
		start = time.time()
		bin_len =Best_Fit(list_of_test_cases[i])
		end = time.time()
		final=end-start
		final = final * multiply_constant
		final = round(final, 2)
		print("Best Fit: "+ str(i))
		print("Time: "+str(final))
		print("Bins: "+ str(bin_len))
		print()
		print()
	
	print()
	print()
	
main()