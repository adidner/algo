import re
import math


def stooge_sort(list_ints):
	
	if len(list_ints) == 2 and list_ints[0] > list_ints[1]:
		temp = list_ints[0]
		list_ints[0] = list_ints[1]
		list_ints[1] = temp
	elif len(list_ints) > 2:
		twothirds = int(math.ceil(len(list_ints) * 2 / 3))
		list_ints[:twothirds] = stooge_sort(list_ints[:twothirds])
		list_ints[(len(list_ints)-twothirds):] = stooge_sort(list_ints[(len(list_ints)-twothirds):])
		list_ints[:twothirds] = stooge_sort(list_ints[:twothirds])
	return list_ints


def read_from_file(fname):
	content = []
	with open(fname) as f:
		content = f.readlines()
		
	for x in range(0,len(content)):
		content[x] = re.sub('\r','',content[x])
		content[x] = re.sub('\n','',content[x])
		content[x] = content[x].split()
		content[x] = list(map(int, content[x]))
	#print(content)
	return content
		
def main():
	
	fname = "data.txt"
	fwrite = "stooge.txt"
	
	
	
	
	
	lists_to_sort = read_from_file(fname)
	
	
	f = open(fwrite, "w")
	for x in range(0, len(lists_to_sort)):
		
		sorted_list = stooge_sort(lists_to_sort[x])
		
		for item in sorted_list:
			f.write("%s " % str(item))
		f.write("\r\n")
	
	
	
	
	


main()