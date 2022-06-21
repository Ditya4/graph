edges = set()
tops = set()
tops_list = []
adjacency_lists = {}
amount_edges = int(input("Enter amount of graph edges\n"))
for edge in range(amount_edges):
    first, second = input("Enter edge(like A B for AB edge):\n").split()
    for top in first, second:
        if top not in tops_list:
            tops_list.append(top)
        if top not in tops:
            tops.add(top)
        if (first, second) not in edges:
            edges.add((first, second))
print(edges)
print(tops)
adjacency_matrix = [[0] * len(tops) for unused_number in range(len(tops))]
print(adjacency_matrix)
for first_index in range(len(tops_list)):
    for second_index in range(len(tops_list)):
        if ((tops_list[first_index], tops_list[second_index]) in edges or
                (tops_list[second_index], tops_list[first_index]) in edges):
            adjacency_matrix[first_index][second_index] += 1
print(adjacency_matrix)

# creating dicts
for index in range(len(tops_list)):
    if tops_list[index] not in adjacency_lists:
        adjacency_lists[tops_list[index]] = set()
for edge in edges:
    adjacency_lists[edge[0]].add(edge[1])
    adjacency_lists[edge[1]].add(edge[0])
print(adjacency_lists)
