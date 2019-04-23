import re

#item class to deal with the item characteristics of price, weight and index
class event:
	def __init__(self, index, start, end):
		self.index = index
		self.start = start
		self.end = end
		
		


#the function used to read in test data from a file		
def ReadTestData(fname):
	content = []
	with open(fname) as f:
		content = f.readlines()
		
	for x in range(0,len(content)):
		content[x] = re.sub('\r','',content[x])
		content[x] = re.sub('\n','',content[x])
	
	return content


	
def FilterIntoClasses(content):
	global_test_cases = []
	current_line = 0
	
	
	
	
	while current_line < len(content):
		list_events = []
		
		#items
		range_end = int(content[current_line])
		print(range_end)
		for i in range(0, range_end):
			current_line+=1
			minilist = content[current_line].split()
			event_var = event(int(minilist[0]), int(minilist[1]), int(minilist[2]))
			list_events.append(event_var)
			
		current_line+=1

				
		global_test_cases.append(list_events)
		
	return global_test_cases


#a function used to make sure the data was correctly read from a file and put into the corresponding classes
def print_filtered_data(global_test_cases):
	print("total number of lists: " + str(len(global_test_cases)))
	for list_item in global_test_cases:
		print("LIST ITEMS")
		print("len this list: "+ str(len(list_item)))
		for i in list_item:
			print("index: "+str(i.index))
			print("start: "+str(i.start))
			print("end: "+str(i.end))
		print("-------------------------------------")


def main():
	fname = "act.txt"
	global_test_cases = []
	
	content = ReadTestData(fname)
	#print(content)
	gloabl_test_cases = FilterIntoClasses(content)
	print_filtered_data(gloabl_test_cases)
	
		
main()