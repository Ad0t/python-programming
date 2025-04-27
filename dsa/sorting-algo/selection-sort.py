arr = [22, 32, 12, 64, 31, 15, 12, 50]

def selectionSort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min]:
                min = j
        # print(arr)
        arr[i], arr[min] = arr[min], arr[i]
    return arr
def selectionSort_unstable(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i+1, len(arr)):
            if arr[j][0] <= arr[min][0]:  
                min = j
        # print(arr)
        arr[i], arr[min] = arr[min], arr[i]
    return arr

def selectionSort_stable(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j][0] < arr[min_index][0]:  # Compare only the first element (key)
                min_index = j
        
        # Instead of swapping, extract the min element and shift elements
        min_value = arr[min_index]
        while min_index > i:
            arr[min_index] = arr[min_index - 1]  # Shift right
            min_index -= 1
        arr[i] = min_value  # Place the min element at its correct position
    
    return arr



# sorted_arr = selectionSort_unstable(arr)
# print("Unstable Sorted Array:", sorted_arr)


if __name__ == '__main__':
    print(f"Before sorting: {arr}\n")
    selectionSort(arr)
    print(f"\nAfter sorting: {arr}")

    arr = [(1, 'A'), (3, 'B'), (1, 'C'), (4, 'D'), (1, 'E'), (4, 'F'), (5, 'G')]
    print("Array:\n", arr)
    sorted_arr = selectionSort_stable(arr)
    print("Stable Sorted Array:\n", sorted_arr)
    arr = [(1, 'A'), (3, 'B'), (1, 'C'), (4, 'D'), (1, 'E'), (4, 'F'), (5, 'G')]
    print("Array:\n", arr)
    sorted_arr = selectionSort_unstable(arr)
    print("Unstable Sorted Array:\n", sorted_arr)