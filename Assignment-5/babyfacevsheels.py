import re


good = "babyface"
bad = "heel"


class node:
	def __init__(self, name):
		self.name = name
		self.type = ""
		self.neighbors = []
	
	def add_neighbor(self, node):
		if node not in self.neighbors:
			self.neighbors.append(node)
			self.neighbors.sort()


class Graph:
	nodes = {}
	
	def add_node(self, node):
		if node.name not in self.nodes:
			self.nodes[node.name] = node
			return True
		else:
			return False
			
	def add_edge(self, start, end):
		if start in self.nodes and end in self.nodes:
			self.nodes[start].add_neighbor(end)
			self.nodes[end].add_neighbor(start)
			return True
		else:
			return False
	
	def get_node(self, name):
		for key in sorted(list(self.nodes.keys())):
			if key == name:
				return key
	
	def print_graph(self):
		for key in sorted(list(self.nodes.keys())):
			print(key + str(self.nodes[key].neighbors))
		
	def print_result(self):
		print("Babyfaces: ", end="")
		for key in sorted(list(self.nodes.keys())):
			if self.nodes[key].type == good:
				print(key + str(self.nodes[key].neighbors),end="")
		print("")
		print("Heels: ", end="")
		for key in sorted(list(self.nodes.keys())):
			if self.nodes[key].type == bad:
				print(key + str(self.nodes[key].neighbors), end="")
		print("")

#the function used to read in test data from a file
def ReadTestData(fname):
	content = []
	with open(fname) as f:
		content = f.readlines()
		
	for x in range(0,len(content)):
		content[x] = re.sub('\r','',content[x])
		content[x] = re.sub('\n','',content[x])
	
	return content

#function used to get the data from array format into events and global test cases
def FilterIntoClasses(content):
	main_graph = Graph()
	size=int(content[0])
	for i in range(1, size):
		new_node = node(str(content[i]))
		main_graph.add_node(new_node)
	
	
	#print(size)
	#print(int(content[size+1]))
	for i in range(1, int(content[size+1])+1):
		minilist = content[i+size+1].split()
		#print(minilist)
		#main_graph.add_edge(main_graph.get_node(minilist[0]), main_graph.get_node(minilist[1]))
		main_graph.add_edge(minilist[0], minilist[1])
	main_graph.print_graph()
	return main_graph

def main():
	
	
	#fname = input("Specify the name of the file to read data from: ")
	fname = "wrestler2.txt"
	
	content = ReadTestData(fname)
	
	FilterIntoClasses(content)





main()