class MaxMin:
    def __init__(self):
        self.max = None
        self.min = None
    def getMaxAndMin(self,arr,start,end):
        if arr == None:
            return
        list=[]
        mid = int((start + end)/2)
        if start == end:
            list.append(arr[start])
            list.append(arr[end])
            return list
        if start == end - 1:
            if arr[start] >= arr[end]:
                list.append(arr[end])
                list.append(arr[start])
            else:
                list.append(arr[start])
                list.append(arr[end])
            return list
        
        LList = self.getMaxAndMin(arr,start,mid)
        RList = self.getMaxAndMin(arr,mid,end)
        max = LList[1] if (LList[1] > RList[1]) else RList[1]
        min = LList[0] if (LList[0] < RList[0]) else RList[0]   
        list.append(min)
        list.append(max)
        return list     
            
if __name__ == "__main__":
    array = [7,3,19,40,4,7,1]
    m = MaxMin()
    result = m.getMaxAndMin(array,0,len(array)-1)
    print(u'最大值为：' + str(result[1]))
    print(u'最小值为：' + str(result[0]))