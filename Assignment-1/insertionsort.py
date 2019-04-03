import re

#this function runs and insertion sort on the data,
#
def sort(list):
	for x in range(0,len(list)):#through all element
		for i in range(x,-1,-1): #backwards through sorted elements
			
			#if I am the first element, I'm arbitrarily sorted
			if x == 0:
				continue
				
			#if I am greater than the left element, I'm arbitrarily sorted
			if list[x] >= list[x-1]:
				continue
				
			#if There is no left element, I belong at the head of the list
			if i == 0:
				temp=list[x]
				del list[x]
				list.insert(0,temp)
				continue
				
			
			#if I am between 2 elements, I belong in between
			if i-1 >= 0:
				if list[i-1] < list[x] and list[x] <= list[i]:
						temp = list[x]
						del list[x]
						list.insert(i,temp)
						continue
	return list


#this function reads data from a file
#the file is assumed to be named data.txt with space seperated integers
def read_from_file(content, fname):
	with open(fname) as f:
		content = f.readlines()
		
	for x in range(0,len(content)):
		content[x] = re.sub('\r','',content[x])
		content[x] = re.sub('\n','',content[x])
		
	return content
	

#this function loops through a list sorting every sub-list located an each indice
#this function then writes the sorted data to a file called insert.txt
def sort_everything(content, fwrite):
	f = open(fwrite, "w")
	
	
	for x in range(0,len(content)):	
	
		current = content[x].split()
		current = list(map(int, current))
		sorted_list = sort(current)
		print(sorted_list)
		
		
		for item in sorted_list:
			f.write("%s " % str(item))
		f.write("\r\n")
		
		print("\n")
	f.close()
	
	
def main():
	fname = "data.txt"
	content = []
	fwrite = "insert.txt"
		
	content = read_from_file(content, fname)
	
	sort_everything(content, fwrite)
	

	
	
main()


