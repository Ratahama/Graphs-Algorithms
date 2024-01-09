def depth_first_search(node, graph, visited, order):
    if node in visited:
        return
    visited.append(node)
    for n in graph[node]:
        depth_first_search(n, graph, visited, order)
    order.append(node)  # tozi red se stiga edva kogato 'n' e posledniqt element na spisuka graph[node]


# INPUT:
graph = {
    7: [19, 21, 14],
    19: [1, 12, 31, 21],
    1: [7],
    12: [],
    31: [21],
    21: [14],
    14: [23, 6],
    23: [21],
    6: []
}  # OUTPUT: 1 12 23 6 14 21 31 19 7

visited = []
order = []
for key in graph:
    depth_first_search(key, graph, visited, order)
print(*order, sep=' ')






# def dfs(node, graph, visited):
#     if node in visited:
#         return
#
#     visited.add(node)
#
#     for child in graph[node]:
#         dfs(child, graph, visited)
#
#     print(node, end=' ')
#
# # INPUT:
# graph = {
#     1: [19, 21, 14],
#     19: [7, 12, 31, 21],
#     7: [1],
#     12: [],
#     31: [21],
#     21: [14],
#     14: [6, 23],
#     23: [21],
#     6: []
# }
# # OUTPUT should be:
# # 7 12 6 23 14 21 31 19 1
# visited = set()  # 'if node in visited:' compares faster when 'visited' is a set() instead of a list
# for node in graph:
#     dfs(node, graph, visited)