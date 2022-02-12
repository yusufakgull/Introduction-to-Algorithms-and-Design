
def inversionCount(arr): 
	temp = [0 for i in range(len(arr))] 
	return mergeSort(arr, 0,len(arr)-1, temp) 


def mergeSort(arr, left, right, temp): 
	mid, inversion_count = 0, 0 
	if (right > left): 
		mid = (right + left) // 2
		inversion_count += mergeSort(arr, left, mid, temp) 
		inversion_count += mergeSort(arr, mid + 1, right,temp) 
		inversion_count += merge(arr, left, mid + 1, right, temp) 
	return inversion_count 

def merge(arr,  left,mid, right, temp): 
	inversion_count = 0	
	l = left # index of left array	
	m = mid # index of right array	
	l2 = left # merged subarray and l2 is index of result
	
	# calculating x[i] > 2x[j] inversions 
	while ((l <= mid - 1) and (m <= right)): 
		if (arr[l] > 2 * arr[m]): 
			inversion_count += (mid - l) 
			m += 1
		else: 
			l += 1

	l = left # index of left array	
	m = mid # index of right array	
	l2 = left # merged subarray and l2 is index of result

	# merge 2 arrays into temp array 
	while (( l <= mid - 1) and (m <= right)): 
		if (arr[l] <= arr[m]): 
			temp[l2] = arr[l] 
			l, l2 = l + 1, l2 + 1
		else: 
			temp[l2] = arr[m] 
			l2, m = l2 + 1, m + 1

	# Copy the remaining elements of the left
	while ( l <= mid - 1): 
		temp[l2] = arr[l] 
		l, l2 = l + 1, l2 + 1

	# Copy the remaining elements of the right 
	while (m <= right): 
		temp[l2] = arr[m] 
		m, l2 = m + 1, l2 + 1
 
	# Copy back the original array 
	for i in range(left, right + 1): 
		arr[i] = temp[i] 

	return inversion_count 


arr = [15, 12, 6, 2, 8] 
print(inversionCount(arr)) 


