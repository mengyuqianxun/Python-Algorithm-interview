def printTrip(inputs):
    reverseinput = dict()
    for i,j in inputs.items():
        reverseinput[j] = i
    start = None
    for i,j in inputs.items():
        if i not in reverseinput:
            start = i
    if start == None:
        print(u'输入不是一趟旅途的车票')
        return
    #从起点出发按照顺序遍历路径
    to = inputs[start]
    print(start + "->" + to,end = '')
    start = to
    to = inputs[start]
    while to != None:
        print(','+start + "->" + to,end = '')
        start = to
        to = inputs.get(start,None)

if __name__ == "__main__":
    inputs = dict()
    inputs["西安"] = "成都"
    inputs["北京"] = "上海"
    inputs["大连"] = "西安"
    inputs["上海"] = "大连"
    printTrip(inputs)
