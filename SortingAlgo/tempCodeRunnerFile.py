def BubbleSort(arr):
    for i in range(len(arr) - 1):
        x = 0
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                x = 1
        if x == 0:
            break
    return arr

arr1 = [2,3,4,12,23,21,22,66,63,33,43,33]
print(BubbleSort(arr1))