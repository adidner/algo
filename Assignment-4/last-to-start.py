import re
import operator



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
		#print(range_end)
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


def last2start(gloabl_test_cases):
	#going through everything in the global list
	i = 1
	print(" ")
	for current_test_case in gloabl_test_cases:
		print("Set "+ str(i))
		#sort by start time greatest to smallest
		sorted_list = sorted(current_test_case, key=operator.attrgetter('start'))
		sorted_list.reverse()
		finallist = []
		
		recursiveelement(sorted_list, finallist)
		
		print("Number of activities selected = "+str(len(finallist)))
		print("Activities:", end=" ")
		finallist.reverse()
		for current in finallist:
			print(str(current.index),end=" ")
		#print_list(finallist)
		print(" ")
		print(" ")
		i+=1
		

def recursiveelement(sorted_list, finallist):
	
	
	
	
	#find the element with the latest (greatest) start time
	greatest = sorted_list[0]
	
	i = 1
	length = len(sorted_list)
	while i < length:
		#eliminate all that conflict with item
		if sorted_list[i].end > greatest.start:
			#print_list(sorted_list)
			del sorted_list[i]
			#print_list(sorted_list)
			length-= 1
		else:
			i+=1
	
			
	#recursively add it to an array and run it again on the resulting array
	del sorted_list[0]
	
	
	
	finallist.append(greatest)
	
	#base case
	if len(sorted_list) == 0:
		return
	
	recursiveelement(sorted_list, finallist)


def print_list(sorted_list):
	for current in sorted_list:
		print(str(current.index)+": "+ str(current.start) + ", " + str(current.end))
	print("----------------")

def main():
	fname = "act.txt"
	global_test_cases = []
	
	content = ReadTestData(fname)
	#print(content)
	gloabl_test_cases = FilterIntoClasses(content)
	#print_filtered_data(gloabl_test_cases)
	last2start(gloabl_test_cases)
		
main()