arr = [22, 32, 12, 64, 31, 15, 50]

def bubbleSort(arr):
    for i in range(len(arr)-1, 0, -1):
        s = 0
        for j in range(0, i):
            if arr[j] > arr[j+1]:
                print(arr)
                arr[j+1], arr[j] = arr[j], arr[j+1]
                s = 1
        if s == 0:
            break
    return arr

if __name__ == '__main__':
    print(f"Before sorting: {arr}\n")
    bubbleSort(arr)
    print(f"\nAfter sorting: {arr}")