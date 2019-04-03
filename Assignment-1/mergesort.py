import re


def merge_sort(list_ints):
	if len(list_ints)==1:
		return list_ints
	else:
		sorted_half_1 = merge_sort(list_ints[:len(list_ints)//2])
		sorted_half_2 = merge_sort(list_ints[len(list_ints)//2:])
		return merge(sorted_half_1, sorted_half_2)


def merge(half_1, half_2):
	counter_1 = 0
	counter_2 = 0
	new_list = []
	while counter_1 < len(half_1) or counter_2 < len(half_2):
		
		if counter_1 > len(half_1)-1:
			new_list.append(half_2[counter_2])
			counter_2+=1
			
		elif counter_2 > len(half_2)-1:
			new_list.append(half_1[counter_1])
			counter_1+=1

		else:
			if half_1[counter_1] < half_2[counter_2]:
				#print("first")
				new_list.append(half_1[counter_1])
				counter_1+=1
			elif half_1[counter_1] >= half_2[counter_2]:
				#print("second")
				new_list.append(half_2[counter_2])
				counter_2+=1
	return new_list


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
	fwrite = "merge.txt"
	
	lists_to_sort = []
	
	
	lists_to_sort = read_from_file(fname)
	
	
	f = open(fwrite, "w")
	for x in range(0, len(lists_to_sort)):
		
		sorted_list = merge_sort(lists_to_sort[x])
		
		for item in sorted_list:
			f.write("%s " % str(item))
		f.write("\r\n")
	
main()