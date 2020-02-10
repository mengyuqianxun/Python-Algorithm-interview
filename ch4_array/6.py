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

if __name__ == "__main__":
    k = 3
    arr = [4,0,1,0,2,3]
    print(u'第' + str(k) + u'小的值为:' + str(getKSmall(arr,k,0,len(arr)-1)))
