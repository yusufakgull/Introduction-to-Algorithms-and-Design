

def Palindrome(string):
    #create 2d dp table
    dp_table = [[False for i in range(len(string))] for j in range(len(string))]
    max_length = 1
    begining =0

    # make diagonal true
    for c in range(len(string)):
        dp_table[c][c] = True
    
    #for length less than 3 check letters are same
    for i in range(len(string) - 1):
        if string[i] == string[i+1]:
            begining = i
            max_length = 2
            dp_table[i][i+1] = True
    #if length bigger than 2 
    for k in range(2, len(string)):
        for i in range(len(string) - k):
            j = i + k
            if dp_table[i + 1][j - 1] and string[i] == string[j]:
                dp_table[i][j] = True
                if k+1 > max_length:
                        begining = i
                        max_length = k+1
    #return longest substring palindrome
    return string[begining:begining+max_length]

print(Palindrome("ABABCabaabaabaBCBCAAAAAA"))