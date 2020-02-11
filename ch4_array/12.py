def reverse(arr,start,end):
    while start < end:
        tmp = arr[start]
        arr[start] = arr[end]
        arr[end] = tmp
        start += 1
        end -= 1

def rightShift(arr,k):
    k %= len(arr)
    reverse(arr,0,len(arr)-k-1)
    reverse(arr,len(arr)-k,len(arr)-1)
    reverse(arr,0,len(arr)-1)

if __name__ == "__main__":
    k = 2
    arr = [1,2,3,4,5,6]
    rightShift(arr,k)
    i = 0
    while i < len(arr):
        print(arr[i],end = ' ')
        i += 1