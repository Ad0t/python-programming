def find_max(arr):
    max = arr[0]
    for i in range(len(arr)):
        if arr[i] > max:
            max = arr[i]
    return max

def count_sort(arr):
    max = find_max(arr)

    # Filling count array of length max+1
    count = [0]*(max+1)
    print(f"Filled count: {count}")

    # Traversing through to find frequency
    for i in range(len(arr)):
        count[arr[i]] += 1
    print(f"Frequency: {count}")

    # Taking prefix sum
    for i in range(1,len(count)):
        count[i] += count[i-1]
    print(f"Prefix sum: {count}")

    output=[0]*(len(arr))
    for i in range(len(arr)-1, -1, -1):
        # print(f"Placing {arr[i]} at position {pos}")
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1

    print(f"Output: {output}")

        

# arr= [1,2,3,4,5,6,6,3,9,2,3,4]
arr = [4,1,2,4,5,2,3]
print(f"Array: {arr}")

x= find_max(arr)
print(f"Max: {x}")
count_sort(arr)