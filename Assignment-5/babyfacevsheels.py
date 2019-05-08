import re
import sys

good = "babyface"
bad = "heel"


class node:
	def __init__(self, name):
		self.name = name
		self.type = ''
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
			#print("in if")
			#print("start: "+ start)
			#print("end: "+ end)
			self.nodes[start].add_neighbor(end)
			self.nodes[end].add_neighbor(start)
			return True
		else:
			return False
	
	
	
	def print_graph(self):
		for key in sorted(list(self.nodes.keys())):
			print(key +": " +self.nodes[key].type +"    " + str(self.nodes[key].neighbors))
		
	def print_result(self):
		print("Yes Possible")
		print("Babyfaces: ", end="")
		for key in sorted(list(self.nodes.keys())):
			if self.nodes[key].type == good:
				print(key + " ",end="")
		print("")
		print("Heels: ", end="")
		for key in sorted(list(self.nodes.keys())):
			if self.nodes[key].type == bad:
				print(key+ " ", end="")
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
	for i in range(1, size+1):
		new_node = node(str(content[i]))
		main_graph.add_node(new_node)
	#print(main_graph.nodes)
	
	for i in range(1, int(content[size+1])+1):
		minilist = content[i+size+1].split()
		#print("minilist: ",end="")
		#print(minilist)
		main_graph.add_edge(minilist[0], minilist[1])
	#main_graph.print_graph()
	return main_graph
	
	
def modified_bfs(main_graph, root):
	currenttype = good
	queue = []
	queue.append(root)
	root.type = currenttype
	currenttype=oppositeofcurrenttype(currenttype)
	
	while len(queue) != 0:
		
		current = queue.pop()
		main_graph.print_graph()
		print()
		for i in current.neighbors:
			current_node=main_graph.nodes[i]
			print()
			print("current_node_name: "+current_node.name)
			print("current_node_type: "+current_node.type)
			print("current_type: "+currenttype)
			print()
			if current_node.type=='':
				current_node.type = currenttype
				#print("appending name: "+current_node.name)
				queue.append(current_node)
			elif current_node.type!=currenttype:
				impossible()
				sys.exit()
		currenttype=oppositeofcurrenttype(currenttype)
		
	return main_graph
	
	
	
	#Looping through ever node
		#if you find one without a color run this again on that node

def impossible():
	print("Impossible")
	

def oppositeofcurrenttype(currenttype):
	if currenttype==good:
		return bad
	elif currenttype==bad:
		return good
	

	
def checkforunexplored(main_graph):
	for key in sorted(list(main_graph.nodes.keys())):
		if main_graph.nodes[key].type == "":
			return main_graph.nodes[key]
	return False

def main():
	
	
	#fname = input("Specify the name of the file to read data from: ")
	fname = "wrestler2.txt"
	
	content = ReadTestData(fname)
	
	main_graph = FilterIntoClasses(content)

	root=main_graph.nodes[str(content[1])]
	
	main_graph = modified_bfs(main_graph,root)
	
	while checkforunexplored(main_graph) != False:
		newroot=checkforunexplored(main_graph)
		modified_bfs(main_graph,newroot)
	main_graph.print_result()


main()