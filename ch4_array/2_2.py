class MaxMin:
    def __init__(self):
        self.max = None
        self.min = None
    def getMaxAndMin(self,arr):
        if arr == None:
            print(u'数组为空')
            return
        lens = len(arr)
        i = 0
        while i < (lens - 1):
            if arr[i] > arr[i+1]:
                tmp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = tmp
            i += 2
        #比较最左边的
        self.min = arr[0]
        i = 2
        while i < lens:
            if arr[i] < self.min:
                self.min = arr[i]
            i += 2
        #比较最右边的
        self.max = arr[1]
        i = 3
        while i < lens:
            if arr[i] > self.max:
                self.max = arr[i]
            i += 2
        if lens % 2 == 1:
            if arr[-1] < self.min:
                self.min = arr[-1]
            if arr[-1] > self.max:
                self.max = arr[-1]

if __name__ == "__main__":
    array = [7,3,19,40,4,7,1]
    m = MaxMin()
    m.getMaxAndMin(array)
    print(u'最大值为：' + str(m.max))
    print(u'最小值为：' + str(m.min))