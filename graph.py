# Add a vertex to the set of vertices and the graph
def add_vertex(v):
  global graph
  global vertices_no
  global vertices
  if v in vertices:
    print("Vertex ", v, " already exists")
  else:
    vertices_no = vertices_no + 1
    vertices.append(v)
    if vertices_no > 1:
        for vertex in graph:
            vertex.append(0)
    temp = []
    for i in range(vertices_no):
        temp.append(0)
        
    graph.append(temp)

# Add an edge between vertex v1 and v2 with edge weight e
def add_edge(v1, v2, e):
    global graph
    global vertices_no
    global vertices
    # Check if vertex v1 is a valid vertex
    if v1 not in vertices:
        print('Vertex ', v1, ' does not exist.')
    # Check if vertex v1 is a valid vertex
    elif v2 not in vertices:
        print("Vertex ", v2, " does not exist.")
    else:
        index1 = vertices.index(v1)
        index2 = vertices.index(v2)
        graph[index1][index2] = e

# Print the graph
def print_graph():
  global graph
  global vertices_no
  for i in range(vertices_no):
    for j in range(vertices_no):
      if graph[i][j] != 0:
        print(vertices[i] ,'->' , vertices[j], 'edge weight:', graph[i][j])
        

# Driver code        
# stores the vertices in the graph
vertices = []
# stores the number of vertices in the graph
vertices_no = 0
graph = []
# Add vertices to the graph
add_vertex("Bangalore")
add_vertex("Chennai")
add_vertex("Mumbai")
add_vertex("Mysore")
# Add the edges between the vertices by specifying
# the from and to vertex along with the edge weights.
add_edge("Bangalore", "Chennai", 1)
add_edge("Bangalore", "Mumbai", 1)
add_edge("Chennai", "Mumbai", 3)
add_edge("Mumbai", "Mysore", 4)
add_edge("Mysore", "Bangalore", 5)
print_graph()
print("Internal representation: ", graph)