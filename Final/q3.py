

def maxRevenue(locations, revenue, no_ads, min_distance, length) : 
	maxRev = [0 for i in range(length+1)] 
	used_ads = 0
	for i in range(1, length + 1) : 
		if (no_ads > used_ads) : 
			if (locations[used_ads] == i) :
				if (i > min_distance) : 
					maxRev[i] = max(maxRev[i - min_distance - 1] +	revenue[used_ads],	maxRev[i - 1])
				else : 
					maxRev[i] = max(maxRev[i - 1],revenue[used_ads]) 
				used_ads += 1 
			else : 
				maxRev[i] = maxRev[i - 1] 		
		else : 
			maxRev[i] = maxRev[i - 1] 
	return maxRev[length] 
	


	
length = 25
locations = [8, 11, 12, 14, 15] 
revenue = [6, 4, 2, 3, 5] 
min_distance = 4
no_ads = len(locations) 
print(maxRevenue(locations, revenue, no_ads, min_distance,length)) 

