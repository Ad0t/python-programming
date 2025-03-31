'''
1. Find the largest element in the array, e.g.- 802. It has three digits, so we will iterate three times, once for each significant place
2. Sort the elements based on the unit place digits(X=0). We use a stable sorting technique, such as counting sort, to sort the digits at each significant place
3. Sort elements based on ones 
4. Sort elements based on tens 
5. Sort elements based on hundreds 
'''

def find_max(arr):
    max = arr[0]
    for i in range(len(arr)):
        if arr[i] > max:
            max = arr[i]
    return max

def count_sort(arr, rad):
    output=[0]*(len(arr))
    count = [0]*(10)
    
    # Filling count array of length max+1
    # print(f"Filled count: {count}")

    # Traversing through to find frequency
    for i in range(len(arr)):
        count[(arr[i]//rad)%10] += 1
    # print(f"Frequency: {count}")

    # Taking prefix sum
    for i in range(1,len(count)):
        count[i] += count[i-1]
    # print(f"Prefix sum: {count}")

    for i in range(len(arr)-1, -1, -1):
        # print(f"Placing {arr[i]} at position {pos}")
        output[count[arr[i]//rad%10] - 1] = arr[i]
        count[arr[i]//rad%10] -= 1

    for i in range(len(arr)):
        arr[i] = output[i]

    print(f"Output: {output}")

def radix_sort(arr):
    max_val = find_max(arr)
    rad = 1
    while max_val//rad > 0:
        count_sort(arr, rad)
        rad *= 10

arr = [170, 45, 75, 90, 802, 24, 2, 66]
ones = [0, 5, 5, 0, 2, 4, 2, 6]
tens = [7, 4, 7, 9, 0, 2, 0, 6]
ones = [1, 0, 0, 0, 8, 0, 0, 0]

radix_sort(arr)
print(f"Sorted array is: {arr}")