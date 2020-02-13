def sort(arr):
    data_count = dict()
    i = 0
    while i < len(arr):
        if arr[i] in data_count:
            data_count[arr[i]] = data_count.get(arr[i]) + 1
        else:
            data_count[arr[i]] = 1
        i += 1
    index = 0
    for key,value in data_count.items():
        i = value
        while i > 0:
            arr[index] = key
            index += 1
            i -= 1

if __name__ == "__main__":
    arr = [15,12,15,2,2,12,2,3,12,100,3,3]
    sort(arr)
    i = 0
    while i < len(arr):
        print(arr[i],end = ' ')
        i += 1