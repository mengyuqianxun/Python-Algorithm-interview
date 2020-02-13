def createArray(a):
    b = [None]*len(a)
    b[0] = 1
    i = 1
    while i < len(a):
        b[i] = b[i-1]*a[i-1]
        i += 1
    b[0] = a[len(a)-1]
    i = len(a) - 2
    while i > 0:
        b[i] *= b[0]
        b[0] *= a[i]
        i -= 1
    return b

if __name__ == "__main__":
    a = [1,1,1,1,1,2,3,4,5]
    b = createArray(a)
    i = 0
    while i < len(b):
        print(b[i],end = ' ')
        i += 1