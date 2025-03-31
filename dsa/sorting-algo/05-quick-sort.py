'''
Lomuto Partition Scheme: Last element
Hoare Partition Scheme: First element
'''
def swap(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b

# print(swap(2,3))

def partition(arr, low, high):
    pivot = arr[low]
    left, right = low+1, high

    while left < right:
        while arr[left] <= pivot and left < high:
            left+=1
        while arr[right] > pivot and right > low:
            right-=1
        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
    arr[low], arr[right] = arr[right], arr[low]
    return right

def quickSort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quickSort(arr, low, pivot-1)
        quickSort(arr, pivot+1, high)
        return arr

if __name__ == '__main__':
    arr = [22, 32, 12, 64, 31, 15, 50]
    print(f"Before sorting: {arr}\n")
    low, high = 0, len(arr) - 1
    quickSort(arr, low, high)
    print(f"After sorting: {arr}")