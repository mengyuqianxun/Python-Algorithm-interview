def getOdd(arr):
    if arr == None:
        return -1
    dic = dict()
    i = 0
    while i < len(arr):
        if arr[i] not in dic:
            dic[arr[i]] = 1
        else:
            dic[arr[i]] = 0 if dic[arr[i]] == 1 else 1
        i += 1
    for m,n in dic.items():
        if n == 1:
            print(int(m),end = ' ')

if __name__ == "__main__":
    arr = [3,5,6,6,5,7,2,2]
    print(u'数组中出现奇数次的数为：')
    getOdd(arr)