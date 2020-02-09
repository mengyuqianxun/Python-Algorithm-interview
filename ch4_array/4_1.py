def getLostNum(arr):
    if arr == None:
        return -1
    a = 0
    b = 0
    i = 0
    while i < len(arr):
        a += arr[i]
        b += (i+1)
        i += 1
    b = b + len(arr) + 1
    return b-a

if __name__ == "__main__":
    arr = [1,4,3,2,7,5]
    print(u'缺失数为：'+str(getLostNum(arr)))