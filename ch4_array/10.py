def findSingle(arr):
    i = 0
    while i < 64:
        result0 = result1 = count0 = count1 =0
        j = 0
        while j < len(arr):
            if (arr[j] & (1<<i)) == 1:
                result1 ^= arr[j]
                count1 += 1
            else:
                result0 ^= arr[j]
                count0 += 1
            j += 1
        i += 1
        if count0 % 2 == 1 and result1 != 0:
            return result0
        if count1 % 2 == 1 and result0 != 0:
            return result1
    return -1

if __name__ == "__main__":
    arr = [6,3,4,5,9,4,3]
    result = findSingle(arr)
    print(result)