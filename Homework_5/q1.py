def sumset_with_dp(input_list):
	sub_list,subSets = [],[]	
	find_all_Subsets(subSets,0, 0, input_list, sub_list)
	return subSets

def find_all_Subsets(subSets,index, sumOfzero, input_list, sub_list) :  
	if (index == len(input_list)) : 
		if (sumOfzero == 0): 
			subSets.append(sub_list)
			return True
		else :
			return False
	if (visited_points[index][sumOfzero + len(visited_points)]) : 
		return dp_table[index][sumOfzero + len(visited_points)] 
	else:
		visited_points.append(1);  
	mem = sub_list.copy()
	sub_list.append(input_list[index])
	dp_table.append(find_all_Subsets(subSets,index + 1, sumOfzero + input_list[index], input_list, sub_list) +   find_all_Subsets(subSets,index + 1, sumOfzero, input_list,mem))
	return dp_table[index][sumOfzero + len(visited_points)]


# input array
arr = [2, 3, -5, -8, 6, -1]

dp_table = [[0 for i in range(len(arr)*50)] for j in range(len(arr)*10)]
visited_points = [[0 for i in range(len(arr)*50)] for j in range(len(arr)*10)]

result = sumset_with_dp(arr)
print("INPUT : ",arr)
if (len(result)==1):
    print("There is no output.")
else:
    for i in range(len(result)-1):
        print("Result ",end='')
        print(i+1,end='')
        print(" = ",end='')
        print(result[i])
    




