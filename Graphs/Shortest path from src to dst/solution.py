def shortest_path(edges, node_A, node_B):
  adj_dict = dict()
  for edge_list in edges:
    if edge_list[0] in adj_dict:
      adj_dict[edge_list[0]].append(edge_list[1])
    else:
      adj_dict[edge_list[0]] = [edge_list[1]]
      
    if edge_list[1] in adj_dict:
      adj_dict[edge_list[1]].append(edge_list[0])
    else:
      adj_dict[edge_list[1]] = [edge_list[0]]
      
  q = []
  dist = 0
  visited = [node_A]
  q.append([node_A, 0])
  
  while len(q) > 0:
    curr, dist = q.pop(0)
    
    if curr == node_B:
      return dist
    
    for node in adj_dict[curr]:
      if node not in visited:
        q.append([node, dist+1])
        visited.append(node)
        
    print()
  return -1
