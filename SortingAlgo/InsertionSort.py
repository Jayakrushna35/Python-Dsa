def InsertionSort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key<arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

arr1 = [2,3,4,12,23,21,22,66,63,33,43,33]
print(InsertionSort(arr1))