import math 

def examine(L, R): 
  j = int(math.log2(R - L + 1)) 
  if pre_calculated[L][j] <= pre_calculated[R - (2* j) + 1][j]: 
    return pre_calculated[L][j] 
  else: 
    return pre_calculated[R - (2* j) + 1][j] 

def create_table(arr, n): 
  for i in range(0, n): 
    pre_calculated[i][0] = arr[i]   
  j = 1
  while (2*j) <= n: 
    i = 0
    while (i + (2*j) - 1) < n: 
      if (pre_calculated[i][j - 1] < 
        pre_calculated[i + (2*(j - 1))][j - 1]): 
        pre_calculated[i][j] = pre_calculated[i][j - 1] 
      else: 
        pre_calculated[i][j] =pre_calculated[i + (2*(j - 1))][j - 1] 
      i += 1
    j += 1    

a = [7, 2, 3, 0, 5, 10, 3, 12, 18] 
n = len(a) 
pre_calculated = [[0 for i in range(n*50)] for j in range(n*50)] 
create_table(a, n) 
print(examine(0, 4)) 
print(examine(4, 7)) 
print(examine(7, 8))