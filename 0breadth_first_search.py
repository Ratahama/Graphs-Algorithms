def bfs(node, graph, visited):
    if node in visited:
        return

    visited.add(node)
    que = [node]

    while que:  # while 'que' has elements in itself
        cur_node = que.pop(0)
        print(cur_node, end=' ')  # OUTPUT: 7 19 21 14 1 12 31 6 23

        for child in graph[cur_node]:
            if child not in visited:
                visited.add(child)
                que.append(child)


graph = {
    7: [19, 21, 14],
    19: [1, 12, 31, 21],
    1: [7],
    12: [],
    31: [21],
    21: [14],
    14: [6, 23],
    6: [],
    23: [21]
}
# visited = [False] * len(graph)  # [False, False, False, ...]  # if 'graph' was a list ,not a dict
visited = set()  # set is an unordered collection of unique elements
# you need to define 'visited' outside of the algorithm and the for loop
# in order for visited to keep on storing the visited nodes,
# otherwise it'll be reset on every iteration of the for loop
for node in graph.keys():
    # breadth_first_search_func(node, graph, visited)
    bfs(node, graph, visited)




# # WITH SET and DEQUE:
# from collections import deque
# def breadth_first_search_func(node, graph, visited):
#     if node in visited:
#         return
#     que = deque([node])
#     visited.add(node)
#     while que:
#         current_node = que.popleft()
#         print(current_node, end=' ')  # OUTPUT: 7 19 21 14 1 12 31 6 23
#         for child in graph[current_node]:
#             if child not in visited:
#                 visited.add(child)
#                 que.append(child)
# graph = {
#     7: [19, 21, 14],
#     19: [1, 12, 31, 21],
#     1: [7],
#     12: [],
#     31: [21],
#     21: [14],
#     14: [6, 23],
#     6: [],
#     23: [21]
# }
# visited = set()  # set is an unordered collection of unique elements
# for node in graph.keys():
#     breadth_first_search_func(node, graph, visited)



# # WITH a DICTIONARY:  (no sets, no deques - just lists and dictionaries)
# def bfs(node, graph, visited):
#     if node in visited.keys():  # works without '.keys()' too
#         return
#     visited[node] = True
#     que = [node]
#     while que:
#         cur_node = que.pop(0)
#         print(cur_node, end=' ')  # OUTPUT: 7 19 21 14 1 12 31 6 23
#         for child in graph[cur_node]:
#             if child not in visited.keys():  # works without '.keys()' too
#                 visited[child] = True
#                 que.append(child)
#
# graph = {
#     7: [19, 21, 14],
#     19: [1, 12, 31, 21],
#     1: [7],
#     12: [],
#     31: [21],
#     21: [14],
#     14: [6, 23],
#     6: [],
#     23: [21]
# }
#
# visited = {}
# for node in graph.keys():  # works without '.keys()' too
#     bfs(node, graph, visited)
