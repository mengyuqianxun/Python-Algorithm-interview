def findTriCommon(arr1,arr2,arr3):
    i = 0
    j = 0
    k = 0
    n1 = len(arr1)
    n2 = len(arr2)
    n3 = len(arr3)
    while  i < n1 and j < n2 and k < n3:
        if arr1[i] == arr2[j] and arr1[i] == arr3[k]:
            print(arr1[i],end = ' ')
            i += 1
            j += 1
            k += 1
        elif arr1[i] < arr2[j]:
            i += 1
        elif arr2[j] < arr3[k]:
            j += 1
        else:
            k += 1

if __name__ == "__main__":
    arr1 = [2,5,12,20,45,85]
    arr2 = [16,19,20,85,200]
    arr3 = [3,4,15,20,39,72,85,190]
    findTriCommon(arr1,arr2,arr3)