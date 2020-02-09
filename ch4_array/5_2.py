def getOdd(arr):
    if arr == None:
        return -1
    c = 0
    i = 0
    while i < len(arr):
        c ^= arr[i]
        i += 1
    tmp = c
    result = c
    index = 0
    while tmp & 1 == 0:
        index += 1
        tmp = tmp >>1
    i = 0
    while i < len(arr):
        if ((arr[i]>>index) & 1) == 1:
            c ^= arr[i]
        i += 1
    print(c,end = ' ')
    print(c^result)

if __name__ == "__main__":
    arr = [3,5,6,6,5,7,2,2]
    print(u'数组中出现奇数次的数为：')
    getOdd(arr)