def minDist(arr,num1,num2):
    mindis = 2**32
    index1 = len(arr)
    index2 = len(arr)
    i = 0
    while i < len(arr):
        if arr[i] == num1:
            if abs(i - index2) < mindis:
                mindis = abs(i - index2)
            index1 = i
        if arr[i] == num2:
            if abs(i-index1) < mindis:
                mindis = abs(i - index1)
            index2 = i
        i += 1
    return mindis


if __name__ == "__main__":
    arr = [4,5,6,4,7,4,6,4,7,8,5,6,4,3,10,8]
    num1 = 4
    num2 = 8
    print(minDist(arr,num1,num2))