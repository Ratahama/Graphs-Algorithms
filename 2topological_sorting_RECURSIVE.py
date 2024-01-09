# # 66% in Judge WITHOUT '*'errors
def topological_sort_recursive(idx: int, graph: dict, removal_order: list):
    # create dict with all nodes and the count of times they are mentioned by the other nodes
    mentions = {}
    for node in graph.keys():
        if node not in mentions:
            mentions[node] = 0
        for val in graph[node]:
            if val not in mentions:
                mentions[val] = 0
            mentions[val] += 1
    # add to order zero mention nodes
    for name, count in mentions.items():
        if count == 0:
            removal_order.append(name)
            del graph[name]

    # print(mentions, order)

    if len(graph) == 0:
        return f"Topological sorting: {', '.join(removal_order)}"
    if idx <= 0:  # idx is just a counter for how many recursive calls we've made so far
        return "Invalid topological sorting"  # if there is a cycle the idx will exceed the original graph's length

    return topological_sort_recursive(idx-1, graph, removal_order)  # reset 'mentions' so that it recalculates


n = int(input())
graph = {}
for _ in range(n):
    key, value = input().split(' ->')
    graph[key] = value.strip().split(', ') if value and value != ' ' else []
# graph = {'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['F'], 'D': ['C', 'F'], 'E': ['D'], 'F': []}
order = []
print(topological_sort_recursive(len(graph), graph, order))



# # INPUT1:
# 6
# A -> B, C
# B -> D, E
# C -> F
# D -> C, F
# E -> D
# F ->
#
# you gotta input it another empty line so that it can take in the 'F' key iteration
# # OUTPUT1:
# Topological sorting: A, B, E, D, C, F

# # INPUT2:
# 5
# IDEs -> variables, loops
# variables -> conditionals, loops, bits
# conditionals -> loops
# loops -> bits
# bits ->
# # OUTPUT2:
# Topological sorting: IDEs, variables, conditionals, loops, bits

# # INPUT3:
# 2
# A -> B
# B -> A
# # OUTPUT3:
# Invalid topological sorting




# # REMOVING explained:
# graph = {'A': ['B', 'C'], 'B':  , 'C': ['F'], 'D': ['C', 'F'], 'E': ['D'], 'F': []}
# mentions = {'A': 0, 'B': 1, 'C': 2, 'D': 2, 'E': 1, 'F': 2}   # remove A, lessen B & C
#         mentions = {'B': 0, 'C': 1, 'D': 2, 'E': 1, 'F': 2}   # remove B, lessen D & E
#                 mentions = {'C': 1, 'D': 1, 'E': 0, 'F': 2}   # remove E, lessen D
#                 mentions = {'C': 1, 'D': 0,         'F': 2}   # remove D, lessen C & F
#                 mentions = {'C': 0,                 'F': 1}   # remove C, lessen F
#                 mentions = {                        'F': 0}   # remove F, print the order in which you removed nodes






# # 66% in Judge WITH one '*'error in the middle
# def topological_sort(graph: dict, removal_order: list):
#     # create dict with all nodes and the count of times they are mentioned by the other nodes
#     mentions = {}
#     for node, children in graph.items():
#         if node not in mentions:
#             mentions[node] = 0
#         for val in children:
#             if val not in mentions:
#                 mentions[val] = 0
#             mentions[val] += 1
#     # print(mentions)
#     # add zero-mention-nodes to 'order'
#     has_zero_mentions = False
#     for name, count in mentions.items():
#         if count == 0:
#             has_zero_mentions = True
#             del graph[name]  # !!!!!!!!!FIX THIS!!!
#             removal_order.append(name)
#     # print(mentions, order)
#
#     if has_zero_mentions == False:
#         if not graph:
#             return f"Topological sorting: {', '.join(removal_order)}"
#         else:
#             return f"Invalid topological sorting"
#
#     # del graph[removal_order[-1]]  # !!!!!!!!!FIX THIS!!!
#     # THERE CAN BE TWO NODES with 0 mentions, but this line will only remove one!
#
#     return topological_sort(graph, removal_order)  # reset 'mentions' so that it recalculates
#
#
# n = int(input())
# graph = {}
# for _ in range(n):
#     line_parts = input().split('->')
#     node = line_parts[0].strip()
#     kids = line_parts[1].strip().split(', ') if line_parts[1] else []
#     graph[node] = kids
# # graph = {'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['F'], 'D': ['C', 'F'], 'E': ['D'], 'F': []}
# order = []
# print(topological_sort(graph, order))
