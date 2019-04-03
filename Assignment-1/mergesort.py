


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
				print("first")
				new_list.append(half_1[counter_1])
				counter_1+=1
			elif half_1[counter_1] >= half_2[counter_2]:
				print("second")
				new_list.append(half_2[counter_2])
				counter_2+=1
	return new_list
	

def split(list_ints):
	print(list_ints[:len(list_ints)//2])
	print(list_ints[len(list_ints)//2:])
	
def main():
	
	list_ints = [3,2,2,1]
	
	sorted_list = merge_sort(list_ints)
	print(sorted_list)
	
main()