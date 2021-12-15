# Adjascency List representation in Python

class AdjNode:
    def __init__(self, value):
        self.vertex = value
        self.next = None


class Graph:
    def __init__(self, num):
        self.V = num
        self.graph = [None] * self.V

    # Add edges
    def add_edge(self, s, d):
        node = AdjNode(d)
        node.next = self.graph[s]
        self.graph[s] = node

        node = AdjNode(s)
        node.next = self.graph[d]
        self.graph[d] = node

    # Print the graph
    def print_agraph(self):
        for i in range(self.V):
            print("Vertex " + str(i) + ":", end="")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.vertex), end="")
                temp = temp.next
            print(" \n")


if __name__ == "__main__":
    V = 5

    # Create graph and edges
    graph = Graph(V)
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(0, 3)
    graph.add_edge(1, 2)

    graph.print_agraph()
    
    
    
    
class Node:
    def __init__(self, data):
        self.key = data
        self.child = []
 
# Function to find number of nodes
# greater than x
def nodesGreaterThanX(root: Node, x: int) -> int:
    if root is None:
        return 0
 
    count = 0
 
    # if current root is greater
    # than x increment count
    if root.key > x:
        count += 1
 
    # Number of children of root
    numChildren = len(root.child)
 
    # recursively calling for every child
    for i in range(numChildren):
        child = root.child[i]
        count += nodesGreaterThanX(child, x)
 
    # return the count
    return count
 
# Driver Code
if __name__ == "__main__":
 
    root = Node(5)
    (root.child).append(Node(1))
    (root.child).append(Node(2))
    (root.child).append(Node(3))
    (root.child[0].child).append(Node(15))
    (root.child[1].child).append(Node(4))
    (root.child[1].child).append(Node(5))
    (root.child[2].child).append(Node(6))
 
    x = 5
 
    print("Number of nodes greater than % d are % d" %
        (x, nodesGreaterThanX(root, x)))    
    
    
    
            if not self.item:
            nuevo_stack=Stack(self.capacidad_maxima)
            nuevo_stack.push(data)
            self.item=nuevo_stack
            Array_Stacks.push(self.item)
        """