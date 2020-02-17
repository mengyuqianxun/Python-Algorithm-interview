def swap(str,a,b):
    tmp = str[a]
    str[a] = str[b]
    str[b] = tmp

def Reverse(str,start,end):
    i = start
    j = end
    while i < j:
        swap(str,i,j)
        i += 1
        j -= 1

def 