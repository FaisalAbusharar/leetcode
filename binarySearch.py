

def binarysearch(arr, target):

    arr.sort()
    print(arr)

    l  = 0
    r = len(arr) - 1

    while l <= r:
        mid = (l+r) // 2
        
        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            l = mid + 1

        elif arr[mid] > target:
            r = mid - 1
        
    return -1
    
    



print(binarysearch(arr=[3,2,7,7,11,15,25], target=11))