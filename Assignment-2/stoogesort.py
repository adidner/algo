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


		
def main():
	input_array = [5,7,1,9,8,11,3,1]
	n = len(input_array)
	stooge_sort(input_array)
	print(input_array)


main()