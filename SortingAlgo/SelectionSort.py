def SelectionSort(arr):
    for i in range(len(arr) - 1):
        min = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[i] :
                min = j
        arr[i],arr[min] = arr[min],arr[i]       
        
    return arr

arr1 = [2,3,4,12,23,21,22,66,63,33,43,33]
print(SelectionSort(arr1))