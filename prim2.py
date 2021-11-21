class graph:
    def __init__(self, nodes=None):
        if nodes is None:
            nodes = {}
        self.nodes = nodes   
        
    def get_nodes(self):
        return list(self.nodes.keys())   
    
    def add_node(self, node):
        if node not in self.nodes:
            self.nodes[node] = []   
            
    def add_edge(self, edge):
        edge = set(edge)
        (weight, node1, node2) = tuple(edge)
        if node1 in self.nodes:
            self.nodes[node1].append((node2, weight))
        else:
            self.nodes[node1] = [(node2, weight)]   
            
    def find_edges(self):
        edge_list = []
        for node in self.nodes:
            for next in self.nodes[node]:
                if {node, next} not in edge_list:
                    edge_list.append({node, next})
        return edge_list
    
    def print_nodes(self):
        print(self.nodes.items())
        
    #def find_weight(self, edge):
        
    
    
    

test = graph()
test.add_node("a")
test.add_node("b")
edge = ("a", "b", 5)
test.add_edge(edge)

test.print_nodes()
    