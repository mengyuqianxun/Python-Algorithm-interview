def MaxArrSum(arr):
    MaxArr = arr[0]
    EndArr = arr[0]
    i = 0
    while i < len(arr):
        EndArr = max(EndArr + arr[i],arr[i])
        MaxArr = max(EndArr,MaxArr)
        i += 1
    return MaxArr

if __name__ == "__main__":
    arr = [1,-2,4,8,-4,7,-1,-5]
    print(u'最大子数组和为：' + str(MaxArrSum(arr)))