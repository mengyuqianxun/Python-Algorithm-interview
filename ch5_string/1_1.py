def swap(str,a,b):
    tmp = str[a]
    str[a] = str[b]
    str[b] = tmp

def Permutation(str,start):
    if str == None or start <0:
        return
    if start == len(str) - 1:
        print(str[:],end = " ")
    else:
        i = start
        while i < len(str):
            swap(str,start,i)
            Permutation(str,start+1)
            swap(str,start,i)
            i += 1
def Permutation_transe(s):
    str = list(s)
    Permutation(str,0)

if __name__ == "__main__":
    s = 'abc'
    Permutation_transe(s)
