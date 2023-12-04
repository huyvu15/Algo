from collections import deque

def is_bipartite(graph, start, color):
    queue = deque()
    
    color[start] = 1
    queue.append(start)
    
    while queue:
        current_vertex = queue.popleft()
        
        for neighbor in range(len(graph)):
            if graph[current_vertex][neighbor] == 1:
                if neighbor not in color:
                    color[neighbor] = 3 - color[current_vertex]  # Gán màu khác với đỉnh hiện tại
                    queue.append(neighbor)
                elif color[neighbor] == color[current_vertex]:
                    return False  # Đồ thị không là đồ thị hai phía
    
    return True  # Đồ thị là đồ thị hai phía

def is_bipartite_graph(adj_matrix, start):
    n = len(adj_matrix)
    color = {}  # Màu của mỗi đỉnh: 1 hoặc 2
    
    if start not in color:
        if not is_bipartite(adj_matrix, start, color):
            return False
    return True

# Example usage:
n = 6  # Số đỉnh
adj_matrix = [
    [0, 1, 1, 0, 0, 0],
    [1, 0, 0, 1, 0, 0],
    [1, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 1],
    [0, 0, 1, 0, 0, 1],
    [0, 0, 0, 1, 1, 0]
]

start_vertex = 0  # Đỉnh bắt đầu

result = is_bipartite_graph(adj_matrix, start_vertex)
print("Is the graph bipartite?", result)
