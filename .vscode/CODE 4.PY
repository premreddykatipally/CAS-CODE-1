def transpose_matrix(matrix): 
    # Use list comprehension to transpose 
    transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))] 
    return transposed 
 
# Example 
matrix = [[1, 2], [3, 4], [5, 6]] 
result = transpose_matrix(matrix) 
print(result)  # Output: [[1, 3, 5], [2, 4, 6]] 