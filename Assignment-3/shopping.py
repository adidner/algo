import re

global_test_cases = []

class item:
	def __init__(self, price, weight):
		self.price = price
		self.weight = weight
		self.index = -1

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
	
def FilterIntoClasses(content):
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
			item_var = item(int(minilist[0]), int(minilist[1]))
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

def print_filtered_data():
	for list_item, list_fam in global_test_cases:
		print("LIST ITEMS")
		for i in list_item:
			print("price: "+str(i.price))
			print("weight: "+str(i.weight))
		print("LIST FAM")
		for j in list_fam:
			print("weight Cap: "+str(j.weight_capacity))
		print("-------------------------------------")

		
		
		
#def napsack(item_array, family_array):



#def prettyprint():	


def main():
	fname = "shopping.txt"
	
	#run the section that gets all the data from the files
	content = ReadTestData(fname)
	FilterIntoClasses(content)
	
	#print_filtered_data()
	
	#for loop through every test case:
		#run the section that does napsack on each person
	







main()