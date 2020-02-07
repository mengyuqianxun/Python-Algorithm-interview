def findDup(array):
    if array == None:
        print(u'数组为空')
    lens = len(array)
    index = 0
    i = 0
    while i < lens:
        if array[i] >= lens:
            return -1
        if array[index] < 0:
            return -array[index]
        index = array[index]
        array[index] *= -1
        if index >= lens:
            return -1
    return -1

if __name__ == '__main__':
    array = [1,3,4,2,5,3]
    print(findDup(array))