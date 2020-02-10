def triMax(a,b,c):
    max = a if a>b else b
    max = c if c>max else max
    return max

def triMin(a,b,c):
    min = a if a<b else b
    min = c if c<min else min
    return min

def getMinDis(a,b,c):
    minDis = 2**32
    i = 0
    j = 0
    k = 0
    while True:
        dis = triMax(abs(a[i]-b[j]),abs(a[i]-c[k]),abs(b[j]-c[k]))
        if dis < minDis:
            minDis = dis
        minele = triMin(a[i],b[j],c[k])
        if minele == a[i]:
            i += 1
            if i == len(a):
                break
        elif minele == b[j]:
            j += 1
            if j == len(b):
                break
        else:
            k += 1
            if k == len(c):
                break
    return minDis

if __name__ == "__main__":
    a = [3,4,5,7,15]
    b = [10,12,14,16,17]
    c = [20,21,23,24,37,30]
    print(u'最小距离为：' + str(getMinDis(a,b,c)))