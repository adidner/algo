import re


def sort(list):
	for x in range(0,len(list)):
		print(list)
		for i in range(x,-1,-1):
			#if I am the first element
			if x == 0:
				print("first")
				continue
			#if I am greater than the left element
			if list[x] >= list[x-1]:
				print("greater than left: "+ str(list[x]) + ", "+ str(list[x-1]))
				continue
			#if There is no left element
			if i == 0:
				print("i of 0")
				print(list)
				temp=list[x]
				del list[x]
				list.insert(0,temp)
				continue
				
			
			#if I am between 2 elements
			if i-1 >= 0:
				if list[i-1] < list[x] and list[x] <= list[i]:
						print("in 2 between")
						print(list)
						temp = list[x]
						del list[x]
						list.insert(i,temp)
						continue
						
						
	return list


def read_from_file(content, fname):
	with open(fname) as f:
		content = f.readlines()
		
	for x in range(0,len(content)):
		content[x] = re.sub('\r','',content[x])
		content[x] = re.sub('\n','',content[x])
		
	return content
	
	
def sort_everything(content):
	for x in range(0,len(content)):	
		print(content[x])
		current = content[x].split()
		current = list(map(int, current))
		sorted_list = sort(current)
		print(sorted_list)
		print("-----------")
	
	
	
def main():
	fname = "data.txt"
	content = []
	
		
	content = read_from_file(content, fname)
	
	sort_everything(content)
	

	
	
main()


