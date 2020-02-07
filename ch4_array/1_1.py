def findDup(array):
    if array == None:
        print(u'数组中无元素')
        return -1
    lens = len(array)
    hashTable = dict()
    i = 0
    while i < lens -1:
        hashTable[i] = 0
        i += 1
    j = 0
    while j < lens:
        if hashTable[array[j]-1] == 0:
            hashTable[array[j]-1] = 1
        else:
            return array[j]
        j += 1
    return -1

if __name__ == '__main__':
    array = [1,3,4,2,5,3]
    print(findDup(array))
