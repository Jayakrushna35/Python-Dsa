def binarySearch(arr,low,high,target):
    if low <= high:
        mid = (low + high)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return binarySearch(arr,low,mid-1,target)
        else: 
            return binarySearch(arr,mid+1,high,target)
    else:
        return -1
    
arr = [1,2,3,4,5,6,7,8,9]
print(binarySearch(arr,0,len(arr),6))



