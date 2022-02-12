def findMissingInt(myarray):
    return findMissing(myarray,len(myarray[0])-1)

def findMissing(myarray,column):
    if column < 0 :
        return 0
    oneBits = []
    zeroBits = []
    for x in myarray :
        if x[column]=='0':
            zeroBits.append(x)
        else :
            oneBits.append(x)
    if( len(zeroBits)<= len(oneBits)):
        num = findMissing(zeroBits,column-1)
        return (num << 1) | 0
    else :
        num =findMissing(oneBits,column-1)
        return (num << 1 ) | 1


input = ['0000',
         '0001',
         '0010',
         '0011',
         '0100',
         '0111',
         '0101',
         '0110',
         #'1000',
         '1001',
         '1010',
         '1011',
         '1100',
         '1101',
         ]

print(findMissingInt(input))