import re
import sys


#Next to do
#make sure the 3 functions are working correctly
#add the timing stuff for them
#do the pretty printing stuff for it


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


def ReadTestData(fname):
	content = []
	with open(fname) as f:
		content = f.readlines()
		
	for x in range(0,len(content)):
		content[x] = re.sub('\r','',content[x])
		content[x] = re.sub('\n','',content[x])
	
	return content



#function used to get the data from array format into events and global test cases
def FilterIntoClasses(content):
	list_of_test_cases = []
	del content[0]
	i=0
	while i < len(content)-3: #loop the number of times we have test cases
		list_items=content[i+2].split()
		list_items = list(map(int, list_items))
		current_test_case = test_case(list_items, int(content[i]))
		#current_test_case.printself()
		list_of_test_cases.append(current_test_case)
		i+=3
	return list_of_test_cases


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
			if current_item + bins[i] < test_case.bin_capacity:
				bins[i] += current_item
				placed = True
				break
		if placed == False:
			bins.append(current_item)
		elif placed == True:
			placed = False
	print(bins)
	
def First_Fit_Dec(test_case):
	bins = []
	
	copy_list_items = test_case.list_items.copy()
	copy_list_items.sort()
	current_item=copy_list_items.pop()
	
	bins.append(current_item)
	placed = False
	while len(copy_list_items)>0:
		current_item=copy_list_items.pop()
		for i in range(0, len(bins)):
			if current_item + bins[i] < test_case.bin_capacity:
				bins[i] += current_item
				placed = True
				break
		if placed == False:
			bins.append(current_item)
		elif placed == True:
			placed = False
	print(bins)


def Best_Fit(test_case):
	bins = []
	copy_list_items = test_case.list_items.copy()
	current_item=copy_list_items.pop()
	bins.append(current_item)
	placed = False
	while len(copy_list_items)>0:
		current_item=copy_list_items.pop()
		left_over_space = 1000000
		current_index = -1
		for i in range(0, len(bins)):
			if current_item + bins[i] < test_case.bin_capacity and test_case.bin_capacity - (current_item + bins[i])< left_over_space :
				#bins[i] += current_item
				current_index = i
				left_over_space = test_case.bin_capacity - (current_item + bins[i])
				placed = True
		if placed == False:
			bins.append(current_item)
		elif placed == True:
			bins[i]+=current_item
			placed = False
	print(bins)



def main():
	
	fname = "bin.txt"
	content = []
	list_of_test_cases = []
	
	#Reading in all test cases from files
	content = ReadTestData(fname)
	list_of_test_cases = FilterIntoClasses(content)	
	
	for i in range(0,len(list_of_test_cases)):
		print("set: " + str(i))
		#run First-fit
		First_Fit(list_of_test_cases[i])
		
		#run First-fit decreasing
		First_Fit_Dec(list_of_test_cases[i])
		
		#run Best-fit
		Best_Fit(list_of_test_cases[i])

main()