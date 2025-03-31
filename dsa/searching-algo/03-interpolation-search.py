arr = [1, 4, 7, 10, 13, 16, 19, 22, 25]
x = int(input("Enter number to be searched: "))

def interpolation_search(arr, x):
    low, high = 0, len(arr) - 1
    while low <= high and x >= arr[low] and x <= arr[high]:
        if low == high:
            if arr[low] == x:
                return low
            return -1
        mid = low + (high - low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1

i = interpolation_search(arr, x)
if i == -1:
    print(f"{x} not found")
else:
    print(f"{x} found at {i}")