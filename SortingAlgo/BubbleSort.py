def BubbleSort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
 
    return arr

arr1 = [2,3,4,12,23,21,22,66,63,33,43,33]
print(BubbleSort(arr1))