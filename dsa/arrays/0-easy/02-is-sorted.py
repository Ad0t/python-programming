def isSorted (arr):
    flag = 1
    for i in range(len(arr)-1):
        if (arr[i] > arr[i+1]):
            flag = 0
    if flag == 1:
        print(f"{arr} is sorted.")
        return True
    else:
        print(f"{arr} is not sorted.")
        return False

if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    isSorted(arr)  # Output: 1
    arr = [1, 7, 9, 3, 5]
    isSorted(arr)  # Output: 0
