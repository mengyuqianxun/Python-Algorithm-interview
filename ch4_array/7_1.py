def minDist(arr,num1,num2):
    mindis = 2**32
    i = 0
    while i < len(arr):
        if arr[i] == num1:
            j = 0
            while j < len(arr):
                if arr[j] == num2:
                    if mindis > abs(i - j):
                        mindis = abs(i - j)
                j += 1
        i += 1
    return mindis

if __name__ == "__main__":
    arr = [4,5,6,4,7,4,6,4,7,8,5,6,4,3,10,8]
    num1 = 4
    num2 = 8
    print(minDist(arr,num1,num2))
                    