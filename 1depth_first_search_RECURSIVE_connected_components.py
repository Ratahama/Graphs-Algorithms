def depth_first_search(idx, graph: list, component: list):
    if visited[idx]:
        return
    visited[idx] = True

    for l in graph[idx]:  # we iterate only through linked nodes
        depth_first_search(l, graph, component)  # recurse through the links of out links

    component.append(idx)

# node_count = int(input())
# graph = []
# for i in range(node_count):
#     row = [int(e) for e in input().split()]
#     graph.append(row)
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
]
visited = [False] * len(graph)  # [False, False, False, ...]
for n in range(len(graph)):
    if visited[n]:  # ako visited[n] e True
        continue
    linked_group = []
    depth_first_search(n, graph, linked_group)
    print(f"Connected component: {' '.join(map(str, linked_group))}")


# # INPUT1:
# # 9 is the count of input lines after, and we DO COUNT the empty line after '0 1 4'
# 9
# 3 6
# 3 4 5 6
# 8
# 0 1 5
# 1 6
# 1 3
# 0 1 4
#
# 2
# # The empty line must make an empty list  >>> []
# # OUTPUT1:
# Connected component: 6 4 5 1 3 0
# Connected component: 8 2
# Connected component: 7


# def depth_first_search(idx, graph, group):
#     if visited[idx]:
#         return
#     visited[idx] = True
#
#     for i in graph[idx]:
#         depth_first_search(i, graph, group)
#     group.append(idx)
#
# nodes_count = int(input())
# graph = []
# for y in range(nodes_count):
#     graph.append([int(c) for c in input().split()])
# # print(*graph, sep="\n")
#
# visited = [False] * nodes_count
# for n in range(len(graph)):  # iterate through nodes 0 to 8
#     if visited[n]:
#         continue
#     linked_nodes = []
#     depth_first_search(n, graph, linked_nodes)  # This changes the linked_nodes list
#     print(f"Connected components: {' '.join(map(str, linked_nodes))}")
#     # print(f"Connected component: {' '.join([str(el) for el in linked_nodes])}")
#     # print(f"Connected components: {linked_nodes}", end=' ')  # DOESN'T WORK EXACTLY RIGHT!




