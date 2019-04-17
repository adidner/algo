import re


#item class to deal with the item characteristics of price, weight and index
class item:
	def __init__(self, price, weight, index):
		self.price = price
		self.weight = weight
		self.index = index

#class family member to deal with the weight capacity and list of item indexs assocaited with each family member
class family_member:
	def __init__(self, weight_capacity):
		self.weight_capacity = weight_capacity
		self.list_of_item_indexs = []
	
	def printer(self):
		for x in range(0, len(self.list_of_item_indexs)):
			print(str(self.list_of_item_indexs[x])+" ", end =" ")
			

#the function used to read in test data from a file		
def ReadTestData(fname):
	content = []
	with open(fname) as f:
		content = f.readlines()
		
	for x in range(0,len(content)):
		content[x] = re.sub('\r','',content[x])
		content[x] = re.sub('\n','',content[x])
	
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

#a function used to make sure the data was correctly read from a file and put into the corresponding classes
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

		
		
# a function meant to run the napsack algorithm on all the test cases and corresponding sub peices		
def run_napsack(global_test_cases):
	
	list_total_prices = []
	for list_item, list_fam in global_test_cases:
		current_total = 0
		for current_fam in list_fam:
			current_fam.list_of_item_indexs, result = napsack(current_fam.weight_capacity, list_item, len(list_item))
			current_total += result
			#print(current_fam.list_of_item_indexs)
		list_total_prices.append(current_total)	
	return global_test_cases,list_total_prices

# the actual running of the napsack algorithm
def napsack(max_weight, list_items, size):
		
	list_indexs = []	
		
	table = [[0 for max_weight in range(max_weight + 1)]for i in range(size + 1)]
	
	for i in range(size+1): 
		
		for w in range(max_weight+1): 
			if i==0 or w==0: 
				
				table[i][w] = 0
				
			elif list_items[i-1].weight <= w: 
				
				table[i][w] = max(
				list_items[i-1].price + table[i-1][w - list_items[i-1].weight], table[i-1][w]
				)
				
			else: 
				
				table[i][w] = table[i-1][w]
	
	result = table[size][max_weight] 
	returner_res = table[size][max_weight]
      
	#the back trace section to regain indexes
	w = max_weight 
	for i in range(size, 0, -1): 
		if result <= 0: 
			break
			
		if result == table[i - 1][w]: 
			continue
		else: 
			list_indexs.insert(0,list_items[i - 1].index + 1)
			result = result - list_items[i - 1].price 
			w = w - list_items[i - 1].weight
			
	return list_indexs, returner_res
			
#print to the file with the format specified in the homework assignment
def prettyprint(global_test_cases,list_total_prices, fwrite):
	
	f = open(fwrite, "w")
	
	counter = 1
	for list_item, list_fam in global_test_cases:
		f.write("Test Case %s \n" % str(counter))
		f.write("Total Price %s \n" % str(list_total_prices[counter-1]))
		f.write("Member Items: \n")
		i = 1
		for current_fam in list_fam:
			f.write("%s: "% str(i))
			for x in current_fam.list_of_item_indexs:
				f.write("%s "% str(x))
			f.write("\n")
			i+=1
		f.write("\n")
		
		counter+=1
		
		
def main():
	#declar global variables like file names and the top level array of test cases
	fname = "shopping.txt"
	fwrite = "results.txt"
	global_test_cases = []
	
	#run the section that gets all the data from the files
	content = ReadTestData(fname)
	
	#put all the data from the file into the list of classes
	global_test_cases = FilterIntoClasses(content, global_test_cases)
	
	#print_filtered_data(global_test_cases)
	
	#run the napsack algorithm and get the return data back in the lists associated witht eh global test array (list_items, list_family)
	#also got back the sum of total value collected by the family
	global_test_cases,list_total_prices = run_napsack(global_test_cases)
	
	#print all the data to a file
	prettyprint(global_test_cases,list_total_prices, fwrite)







main()