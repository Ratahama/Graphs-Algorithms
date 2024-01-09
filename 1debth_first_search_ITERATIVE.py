# def breadth_first_search_iterative(node, graph, visited, component):
#     que = [node]
#     while que:
#         current_node = que.pop(0)
#         if visited[current_node]:
#             continue
#         component.append(current_node)
#         visited[current_node] = True
#         # print(current_node, end=' ')
#         for child in graph[current_node]:
#             # we stack the new horizonts seen from our 'current_node' on our 'que'
#             if not visited[child]:
#                 # 'and not in que:' may optimize(or slow down) the conditional statement
#                 que.append(child)
#
# graph = [
#     [3, 6],
#     [3, 4, 5, 6],
#     [8],
#     [0, 1, 5],
#     [1, 6],
#     [1, 3],
#     [0, 1, 4],
#     [],
#     [2]
# ]
# # # OUTPUT:
# # Connected component: 0 3 6 1 5 4
# # Connected component: 2 8
# # Connected component: 7
#
# visited = [False] * len(graph)  # [False, False, False, ...]
# for n in range(len(graph)):
#     if visited[n]:
#         continue
#     component = []
#     breadth_first_search_iterative(n, graph, visited, component)
#     print(f"Connected component: {' '.join(map(str, component))}")



def depth_first_search_iterative(node, graph, visited, component):  # NOT QUITE a recursive imitation
    que = [node]

    while que:
        current_node = que.pop()
        if visited[current_node]:
            continue
        component.append(current_node)
        visited[current_node] = True
        for child in graph[current_node]:

            # we stack the new horizonts seen from our 'current_node' on our 'que'
            if not visited[child]:
                # 'and not in que:' may optimize(or slow down) the conditional statement
                que.append(child)


graph = [
    [3, 6],
    [3, 4, 5, 6],
    [8],
    [0, 1, 5],
    [1, 6],
    [1, 3],
    [0, 1, 4],
    [],
    [2]
]  # 0 3 1 4 6 5
# # OUTPUT should be:
# Connected component: 6 4 5 1 3 0
# Connected component: 8 2
# Connected component: 7


visited = [False] * len(graph)  # [False, False, False, ...]
for n in range(len(graph)):
    if visited[n]:
        continue
    component = []
    depth_first_search_iterative(n, graph, visited, component)
    print(f"Connected component: {' '.join(map(str, component))}")







