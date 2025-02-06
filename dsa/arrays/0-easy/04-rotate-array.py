def rotateArray(arr):
    temp = arr[0]
    for i in range(1, len(arr)):
        arr[i-1] = arr[i]
    arr[len(arr)-1] = temp

def rotateArrayByK(arr, k):
    n = len(arr)
    k = k % len(arr)
    temp = [0]*k
    for i in range(k):      # stores in temporary array
        # [1,2,3,4,5,6,7]
        temp[i] = arr[i]

    for i in range(k, n):
        # arr[4-4] = arr[4], arr[5-4] = arr[5], arr[6-4] = arr[6]
        arr[i - k] = arr[i]
    
    for i in range(n-k, n): # [7-4, 7]
        # arr[3] = temp[3-(7-4)], arr[4] = temp[4-(7-4)],..... 
        arr[i] = temp[i - (n - k)]

def reverseArray(arr, start, end):
    while (start <= end):
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start += 1
        end -= 1

def rotateArrayByKO(arr, k):
    reverseArray(arr, 0, (len(arr) - k) - 1)
    reverseArray(arr, len(arr) - k, len(arr) - 1)
    reverseArray(arr, 0, len(arr) - 1)
    


if __name__ == '__main__':
    arr = [1,2,3,4,5,6,7]
    print(f"Original Array: {arr}")
    # rotateArray(arr)
    # rotateArrayByK(arr, 4)
    rotateArrayByKO(arr, 4)
    print(f"Rotated Array: {arr}")