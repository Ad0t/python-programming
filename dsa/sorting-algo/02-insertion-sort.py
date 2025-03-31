arr = [22, 32, 12, 64, 31, 15, 50]

def insertionSort(arr):
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j - 1]:
            print(arr)
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1
    return arr

if __name__ == '__main__':
    print(f"Before sorting: {arr}")
    insertionSort(arr)
    print(f"After sorting: {arr}")