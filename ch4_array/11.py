def getKSmall(arr,k,start,end):
    i = start
    j = end
    median = arr[i]
    while i < j:
        while i < j and arr[j] > median:
            j -= 1
        if i < j:
            arr[i] = arr[j]
        while i < j and arr[j] <= median:
            i += 1
        if i < j:
            arr[j] = arr[i]
    arr[i] =  median

    if i - start == k - 1:
        return arr[i]
    elif i - start > k-1:
        return getKSmall(arr,k,start,i-1)
    else:
        return getKSmall(arr,k-(i-start)-1,i+1,end)

def getMid(arr):
    start = 0
    end = len(arr)-1
    if len(arr) % 2 ==1:
        mid = (len(arr) + 1)/2
        return getKSmall(arr,mid,start,end)
    else:
        a = getKSmall(arr,len(arr)/2,start,end)
        b = getKSmall(arr,len(arr)/2+1,start,end)
        return (a+b)/2

if __name__ == "__main__":
    arr = [7,5,3,1,11,9]
    print(getMid(arr))
