def find_min_sum_path(triangle): 
      
    min_path = [None] * len(triangle)
    last_row = len(triangle) - 1
      
    # For the bottom row
    for i in range(len(triangle[last_row])):  
        min_path[i] = triangle[last_row][i]
    # calculation    
    for i in range(len(triangle) - 2, -1,-1):  
        for j in range( len(triangle[i])):
            min_path[j] = triangle[i][j] + min(min_path[j],min_path[j + 1])    
    return min_path[0]
  
 
q2 = [[ 2 ], 
    [5, 4 ], 
   [1, 4, 7 ],
  [8,6, 9, 6 ]] 
result = find_min_sum_path(q2)
print(result) 
  
