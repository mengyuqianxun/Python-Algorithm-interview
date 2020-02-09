def getMin(arr,start,end):
    if start == end:
        return arr[start]
    mid = int((start + end)/2)
    if arr[mid] < arr[mid-1]:
        return arr[mid]
    if arr[mid+1] < arr[mid]:
        return arr[mid+1]
    elif arr[end] > arr[mid]:
        return getMin(arr,start,mid - 1)
    elif arr[mid] > arr[start]:
        return getMin(arr,mid + 1,end)
    else:
        return min(getMin(arr,start,mid - 1),getMin(arr,mid + 1,end))

if __name__ == "__main__":
    array1 = [5,6,1,2,3,4]
    mins = getMin(array1,0,len(array1)-1)
    print(mins)
    array2 = [1,1,0,1]
    mins = getMin(array2,0,len(array2)-1)
    print(mins)