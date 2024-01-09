# # 100% in Judge
def topological_sort(graph: dict):  # ALL IN ONE FUNCTION!!!!!!!!!!Like in my dreams! XD im dead
    dependencies_count = {}
    for node, children in graph.items():
        if node not in dependencies_count:
            dependencies_count[node] = 0
        for val in children:
            if val not in dependencies_count:
                dependencies_count[val] = 0
            dependencies_count[val] += 1

    removal_order = []
    while dependencies_count:

        # start # SEEKING THE ZERO DEPENDENCIES NODE ####################################################
        for node, count in dependencies_count.items():
            if count == 0:
                node2remove = node
                break
        else:  # this 'else'-condition will be met only when the for loop above does NOT get BROKEN
            return "Invalid topological sorting"  # there is a cycle, can't execute topological_sort!!!
        # enduu # SEEKING THE ZERO DEPENDENCIES NODE #####################################################

        dependencies_count.pop(node2remove)
        removal_order.append(node2remove)
        for child in graph[node2remove]:
            dependencies_count[child] -= 1

    return f"Topological sorting: {', '.join(removal_order)}"


n = int(input())
graph = {}
for _ in range(n):
    key, value = input().split(' ->')
    graph[key] = value.strip().split(', ') if value and value != ' ' else []
# graph = {'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['F'], 'D': ['C', 'F'], 'E': ['D'], 'F': []}
print(topological_sort(graph))



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





# # 2nd SOLUTION(Bat Nasko) segmented in separate functions:
def find_dependencies(grapha: dict):
    dependencies = {}
    for node, children in grapha.items():
        if node not in dependencies:
            dependencies[node] = 0
        for val in children:
            if val not in dependencies:
                dependencies[val] = 0
            dependencies[val] += 1
    return dependencies


def zero_dependencies_node(dependencies_count: dict):
    for node, count in dependencies_count.items():
        if count == 0:
            return node
    return 'No zero node'


n = int(input())
graph = {}
for _ in range(n):
    # line_parts = input().split('->')
    # node = line_parts[0].strip()
    # children = line_parts[1].strip().split(', ') if line_parts[1] else []
    # graph[node] = children
    key, value = input().split(' ->')
    graph[key] = value.strip().split(', ') if value and value != ' ' else []
# graph = {'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['F'], 'D': ['C', 'F'], 'E': ['D'], 'F': []}

dependencies_count = find_dependencies(graph)
has_cycles = False
removal_order = []

while dependencies_count:  # ne pishsi 'len(graph) > 0' tuk, PROSTO NE!
    node2remove = zero_dependencies_node(dependencies_count)
    if node2remove == 'No zero node':
        has_cycles = True
        break
    dependencies_count.pop(node2remove)
    removal_order.append(node2remove)
    for child in graph[node2remove]:
        dependencies_count[child] -= 1

if has_cycles:
    print("Invalid topological sorting")
else:
    print(f"Topological sorting: {', '.join(removal_order)}")





