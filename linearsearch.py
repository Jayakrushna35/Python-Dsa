def Search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

print(Search([1,2,3,4,5,6,11,22,33,43,24,22],22))