# from collections import deque
#
#
# def bfs(node, graph, visited):
#     if node in visited:
#         return
#     queue = deque([node])
#     visited.add(node)
#
#     while queue:
#         current_node = queue.popleft()
#         print(current_node, end=' ')
#
#         for child in graph[current_node]:
#             if child not in visited:
#                 visited.add(child)
#                 queue.append(child)
#
#
# graph = {
#     7: [19, 21, 14],
#     19: [1, 12, 31, 21],
#     1: [7],
#     12: [],
#     31: [21],
#     21: [14],
#     14: [23, 6],
#     6: [],
#     23: [21]
# }
#
# visited = set()
#
# for node in graph:
#     bfs(node, graph, visited)




def breadth_first_search(node, graph, result, visited):
    if node in visited:
        return 'Node already visited'
    que = []
    que.append(node)
    while que:
        current_node = que.pop(0)
        visited.add(current_node)
        result.append(current_node)
        # print(current_node, end=' ')
        for child in graph[current_node]:
            if child not in visited:
                visited.add(child)
                que.append(child)
    # return ' '.join(map(str, result))
    print(*result, sep=' ')


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

visited = set()
result = []
for key in graph:  # if there are separate node-groups in the graph that do not connect this for loop will find and print them on separate lines
    breadth_first_search(key, graph, result, visited)

