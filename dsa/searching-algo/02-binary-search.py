arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

x = int(input("Enter the number to be searched: "))

def binary_search(arr, x):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1

i = binary_search(arr, x)
if i == -1:
    print(f"{x} not found")
else:
    print(f"{x} found at {i}")