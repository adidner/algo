import re



class item:
	def __init__(self, price, weight, index):
		self.price = price
		self.weight = weight
		self.index = index

class family_member:
	def __init__(self, weight_capacity):
		self.weight_capacity = weight_capacity
		self.list_of_item_indexs = []
	
	def printer(self):
		for x in range(0, len(self.list_of_item_indexs)):
			print(str(self.list_of_item_indexs[x])+" ", end =" ")
		
def ReadTestData(fname):
	content = []
	with open(fname) as f:
		content = f.readlines()
		
	for x in range(0,len(content)):
		content[x] = re.sub('\r','',content[x])
		content[x] = re.sub('\n','',content[x])
	
	#print(content)
	return content
	
def FilterIntoClasses(content, global_test_cases):
	current_line = 1
	number_test_cases = content[0]
	#test cases
	for x in range(0,int(number_test_cases)):
		
		list_fam = []
		list_item = []
		#items
		for i in range(0, int(content[current_line])):
			current_line+=1
			minilist = content[current_line].split()
			item_var = item(int(minilist[0]), int(minilist[1]), i)
			list_item.append(item_var)
			
		current_line+=1
		#family members
		for c in range(0, int(content[current_line])):
			current_line+=1
			carryingcapacity = content[current_line]
			fam = family_member(int(carryingcapacity))
			list_fam.append(fam)
		current_line+=1
			
		global_test_cases.append((list_item, list_fam))
		
	return global_test_cases

def print_filtered_data(global_test_cases):
	for list_item, list_fam in global_test_cases:
		print("LIST ITEMS")
		for i in list_item:
			print("price: "+str(i.price))
			print("weight: "+str(i.weight))
			print("index: "+str(i.index))
		print("LIST FAM")
		for j in list_fam:
			print("weight Cap: "+str(j.weight_capacity))
		print("-------------------------------------")

		
		
		
def run_napsack(global_test_cases):
	for list_item, list_fam in global_test_cases:
		for current_fam in list_fam:
			napsack(current_fam, current_fam.weight_capacity, list_item)

def napsack(current_fam, weight_capacity, list_items, current_size):
	if len(list_items) == 0 or weight_capacity == 0:
		return 
	
	
	#run recursive part of napsack and put the values back into the index
	#tracking part of the class
	
	
	#if list_items[n-1].weight > weight_capacity:
	#	return napsack(current_fam, weight_capacity,list_items, n-1)
	#else:
	#	return max(list_items[n-1] + napsack(current_fam, weight_capacity - list_items[n-1], weight_capacity, list_items, n-1), napsack(current_fam, weight_capacity,list_items, n-1))
	
	
#def prettyprint():	


def main():
	fname = "shopping.txt"
	global_test_cases = []
	
	#run the section that gets all the data from the files
	content = ReadTestData(fname)
	global_test_cases = FilterIntoClasses(content, global_test_cases)
	
	print_filtered_data(global_test_cases)
	
	run_napsack(global_test_cases)
	







main()