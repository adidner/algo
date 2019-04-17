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
	
	list_total_prices = []
	for list_item, list_fam in global_test_cases:
		current_total = 0
		for current_fam in list_fam:
			current_fam.list_of_item_indexs, result = napsack(current_fam.weight_capacity, list_item, len(list_item))
			current_total += result
			print(current_fam.list_of_item_indexs)
		list_total_prices.append(current_total)	
	return global_test_cases,list_total_prices
			
def napsack(W, list_items, n):
		
	list_indexs = []	
		
	K = [[0 for w in range(W + 1)]for i in range(n + 1)]
	
	for i in range(n + 1): 
		for w in range(W + 1): 
			if i == 0 or w == 0: 
				K[i][w] = 0
			elif list_items[i - 1].weight <= w: 
				K[i][w] = max(list_items[i - 1].price  
				+ K[i - 1][w - list_items[i - 1].weight], 
				K[i - 1][w]) 
			else: 
				K[i][w] = K[i - 1][w]
	
	res = K[n][W] 
	returner_res = K[n][W]
      
	w = W 
	for i in range(n, 0, -1): 
		if res <= 0: 
			break
			
		if res == K[i - 1][w]: 
			continue
		else:
			#print("item Index: "+str(list_items[i - 1].index + 1)) 
			list_indexs.insert(0,list_items[i - 1].index + 1)
			res = res - list_items[i - 1].price 
			w = w - list_items[i - 1].weight
			
	return list_indexs, returner_res
			

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
	fname = "shopping.txt"
	fwrite = "results2.txt"
	global_test_cases = []
	
	#run the section that gets all the data from the files
	content = ReadTestData(fname)
	global_test_cases = FilterIntoClasses(content, global_test_cases)
	
	#print_filtered_data(global_test_cases)
	
	global_test_cases,list_total_prices = run_napsack(global_test_cases)
	
	prettyprint(global_test_cases,list_total_prices, fwrite)







main()