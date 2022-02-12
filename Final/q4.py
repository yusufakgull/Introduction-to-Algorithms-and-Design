
def max_cost_index(arr):
    row,col = 0,0
    max_cost = -2
    for i in range(0, len(arr)):
        for j in range(0, len(arr)):
            if max_cost < arr[i][j]:
                max_cost = arr[i][j]
                row = i
                col = j
    return max_cost,row,col


def max_cost(cost_arr):
    length = len(cost_arr)
    result_arr = [[0 for i in range(length)] for j in range(length)]
    for i in range(0, length**2):
        max_cost,row,col = max_cost_index(cost_arr)
        if max_cost > 0:
            row_count = 0
            for j in range(0, length):
                if cost_arr[j][col] > 0:
                    row_count += 1
            col_count = 0
            for j in range(0, length):
                if cost_arr[row][j] > 0:
                    col_count += 1
            if row_count > 1 and col_count > 1:
                cost_arr[row][col] = -1
            else:
                result_arr[row][col] = cost_arr[row][col]
                cost_arr[row][col] = 0
                for j in range(0, length):
                    if cost_arr[j][col] != 0:
                        cost_arr[j][col] = -1
                for j in range(0, length):
                    if cost_arr[row][j] != 0:
                        cost_arr[row][j] = -1
    return result_arr



array = [[40, 27, 75, 50],
         [62, 20, 8, 45],
         [37, 98, 60, 94],
         [94, 33, 6, 64]]
arrx = max_cost(array)
for i in arrx:
    print(i)



