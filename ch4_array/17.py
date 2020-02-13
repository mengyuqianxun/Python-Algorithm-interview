'''
param t 每台服务器处理的时间
param n 任务的个数
return 各个服务器执行完任务所需的时间
'''
def calculate_process_time(t,n):
    if t == None or n <= 0:
        return None
    m = len(t)
    proTime = [0] * m
    i = 0
    while i < n:
        minTime = proTime[0] + t[0]
        minIndex = 0
        j =1
        while j < m:
            if minTime > proTime[j] + t[j]:
                minTime = proTime[j] + t[j]
                minIndex = j
            j += 1
        proTime[minIndex] += t[minIndex]
        i += 1
    return proTime

if __name__ == "__main__":
    t = [7,10]
    n = 6
    proTime = calculate_process_time(t,n)
    if proTime == None:
        print(u'分配失败')
    else:
        totalTime = proTime[0]
        i = 0
        while i < len(proTime):
            print(u'第' + str(i +1) + u'台服务器有' + str(proTime[i]/t[i]) + u'个任务，执行总时间为：' + str(proTime[i]))
            if proTime[i] > totalTime:
                totalTime = proTime[i]
            i += 1
        print(u'执行完所有任务所需时间为' + str(totalTime))