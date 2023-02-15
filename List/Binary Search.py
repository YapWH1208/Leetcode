def BinarySearch(arr, num):
    arr.sort()
    left = 0
    right = len(arr) - 1

    while left <= right:
        middle = (left + right) // 2
        if arr[middle] > num:
            right = middle - 1
        elif arr[middle] < num:
            left = middle + 1
        else:
            return middle
    return -1


list1 = [1,2,2,5,4,7,8,9,12,15,48,96]
target1 = 48

print(BinarySearch(list1, target1))