def removingDupes(arr):
    if arr == []:
        return 0
    i = 0
    for j in range(1, len(arr)):
        if arr[i] != arr[j]:
            i += 1
            arr[i] = arr[j]
    return i + 1

if __name__ == '__main__':
    arr = [1, 1, 2, 2, 3, 4, 4, 4, 5]
    new_length = removingDupes(arr)
    print(arr)
    print(arr[:new_length])  # Output: [1, 2, 3, 4, 5]
    print(new_length)  # Output: 5