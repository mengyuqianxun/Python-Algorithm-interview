def is_allocable(d,p):
    dIndex = 0
    i = 0
    while i < len(p):
        while dIndex < len(d) and p[i] > d[dIndex]:
            dIndex += 1
        if dIndex >= len(d):
            return False
        d[dIndex] -= p[i]
        i += 1
    return True

if __name__ == "__main__":
    d =[120,120,120]
    p = [60,60,80,20,80]
    if is_allocable(d,p):
        print(u'分配成功')
    else:
        print(u'分配失败')
