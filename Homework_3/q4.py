import random

def partition(arr,low,high):
    pivot = arr[high]
    count=0
    i =low-1 
    for j in range(low , high):
        if   arr[j] < pivot:
            i += 1
            arr[i],arr[j] = arr[j],arr[i]
            count += 1
    arr[i+1],arr[high] = arr[high],arr[i+1]
    count+=1
    return i+1,count

def quickSort(arr,low,high):
    count=0
    if low < high:
        pi,partition_count = partition(arr,low,high)
        count+=partition_count
        count+=quickSort(arr, low, pi-1)
        count+=quickSort(arr, pi+1, high)
    return count

def insertionSort(arr):
    count=0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j] :
                count+=1
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key
    return count


def main():
     avg_quick=0
     avg_insertion=0
     for i in range(1,21): #range is test count (20)
         arr_1=[]
         arr_2=[]
         for j in range(i*10): #array size (10,20,30,40,...,190,200)
             randomNum=random.randint(0,1000)
             arr_1.append(randomNum)
             arr_2.append(randomNum)
         swap_count=quickSort(arr_1,0,i*10-1) 
         avg_quick+=swap_count
         print("QuickSort swap count for size ",i*10,"     : ",end = '')
         print(swap_count)
         swap_count=insertionSort(arr_2)
         avg_insertion+=swap_count
         print("InsertionSort swap count for size ",i*10," : ",end = '')
         print(swap_count)
     avg_quick/=20 # 20 array
     avg_insertion/=20 #20 array
     print("----------------------------------")
     print("Average QuickSort swap count    : ",avg_quick)
     print("Average InsertionSort swap count: ",avg_insertion)

main()


