def knapsack(items_count, values, weights,W):
	dp_table = [0 for i in range(W + 1)]
	for i in range(W + 1):
		for j in range(items_count):
			if (weights[j] <= i):
				dp_table[i] = max(dp_table[i], dp_table[i - weights[j]] + values[j])
	return dp_table[W]

W = 9
values = [10, 4, 3]
weights = [5, 4, 2]
print(knapsack(len(values), values, weights,W))

