class pair:
    def __init__(self,first,second):
        self.first = first
        self.second = second


def findPairs(arr):
    #键为数对和，值为数对
    pairDict = dict()
    n = len(arr)
    #遍历数组中所有可能的数对
    i = 0
    while i < n:
        j = i + 1
        while j < n:
            sums = arr[i] + arr[j]
            pair_a = pair(arr[i],arr[j])
            if sums not in pairDict:
                pairDict[sums] = pair_a
            else:
                p = pairDict[sums]
                print("(" + str(p.first) + "," +str(p.second) + ")  " "(" + str(arr[i]) + "," +str(arr[j]) + ")")
                return True
            j += 1
        i += 1
    return False


if __name__ == "__main__":
    arr = [3,4,7,10,20,9,8]
    findPairs(arr)