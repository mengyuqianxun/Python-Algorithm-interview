def findDup(array):
    if array == None:
        print(u'该数组为空')
        return -1
    lens = len(array)
    result = 0
    i = 0
    while i < lens:
        result ^= array[i]
        i += 1
    j = 1
    while j < lens:
        result ^= j
        j += 1
    return result

if __name__ == '__main__':
    array = [1,3,4,2,5,3]
    print(findDup(array))