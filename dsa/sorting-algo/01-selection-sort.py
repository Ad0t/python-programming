arr = [12, 32, 22, 64, 31, 15, 50]

def selectionSort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]
    return arr

if __name__ == '__main__':
    print(f"Before sorting: {arr}")
    selectionSort(arr)
    print(f"After sorting: {arr}")
    