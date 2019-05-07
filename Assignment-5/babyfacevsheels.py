
good = "babyface"
bad = "heel"


class node:
	def __init__(self, name):
		self.name = name
		self.type = ""
		self.neighbors = []
	
	def add_neighbor(self, node):
		if node not in self.neighbors:
			self.neightbors.append(node)
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
	
	def print_graph(self):
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
	


def main():
	fname = input("Specify the name of the file to read data from: ")

	content = ReadTestData(fname)







main()