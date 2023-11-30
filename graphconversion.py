
# Function to convert Edge List to Adjacency List

from collections import defaultdict
def edge_list_to_adjacency_list(edge_list):
    adj_list = defaultdict(list)

	# Write your code here to convert the edge list to an adjacency list.

    for source, des in edge_list:
        adj_list[source].append(des)
    return adj_list

# Test case
edge_list_sample = [(0, 1), (0, 2), (1, 2), (2, 0), (2, 3), (3, 3)]

# --- Student Section to Write Code ---
# Write your code for the conversion here
result_adj_list = edge_list_to_adjacency_list(edge_list_sample)
expected_result = {
    0: [1, 2],
    1: [2],
    2: [0, 3],
    3: [3]
}

# Print the result for verification
print("Result:", result_adj_list)
if result_adj_list == expected_result:
    print("Correct! Your code produced the expected result.")
else:
    print("Incorrect! Please try again")






# Function to convert Adjacency List to Adjacency Matrix
def adjacency_list_to_matrix(adj_list):

# Write your code here to convert the adjacency list to an adjacency matrix
    adj_matrix = [[0 for _ in range(4) ]for _ in range(4)]
    
    for i in range(4):
        for j in adj_list[i]:
            adj_matrix[i][j] = 1

    return adj_matrix

# Test case
adj_list_sample = {
    0: [1, 2],
    1: [2],
    2: [0, 3],
    3: [3]
}
print("hello")
result_matrix = adjacency_list_to_matrix(adj_list_sample)
expected_result = [
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [1, 0, 0, 1],
    [0, 0, 0, 1]
]

# Print the result for verification
print("Result:", result_matrix)
if result_matrix == expected_result:
    print("Correct! Your code produced the expected result.")
else:
    print("Incorrect! Please try again")



# Function to convert Adjacency Matrix to Adjacency List
from collections import defaultdict
def adjacency_matrix_to_adjacency_list(adj_matrix):
    adj_list = defaultdict(list)
  

    # Write your code here to convert the adjacency matrix to an adjacency list
    # Your code goes here

    for row in range(len(adj_matrix)):
        for col in range(len(adj_matrix[0])):
            if adj_matrix[row][col] == 1:
                adj_list[row].append(col)

    return adj_list  # Return the adjacency list

# Test case
adj_matrix_sample = [
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [1, 0, 0, 1],
    [0, 0, 0, 1]
]

# --- Student Section to Write Code ---
# Write your code for the conversion here
result_adj_list = adjacency_matrix_to_adjacency_list(adj_matrix_sample)
expected_result = {
    0: [1, 2],
    1: [2],
    2: [0, 3],
    3: [3]
}

# Print the result for verification
print("Result:", result_adj_list)
if result_adj_list == expected_result:
    print("Correct! Your code produced the expected result.")
else:
    print("Incorrect! Please try again")

