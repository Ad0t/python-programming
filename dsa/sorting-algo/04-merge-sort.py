'''
Merging is the process of combining 2 sorted list/array such a way that the resultant list/array is also in sorted array.
'''
a = [1,3,5,7]
b = [2,4,6,8, 9,10,11,12]
def merging(a,b):
    res = []
    i, j= 0, 0
    '''
    loop runs till one of the list is exhausted, by append 
    '''
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            res.append(a[i])
            i+=1
        else:
            res.append(b[j])
            j+=1

    if i == len(a):
        for m in b[j:]:
            res.append(m)
    elif j == len(b):
        for m in a[i:]:
            res.append(m)
    return res

# print(merging(a,b))



arr = [22, 32, 12, 64, 31, 15, 50]


def merge(arr, low, mid, high):
    temp = []
    left, right = low, mid + 1
    while (left <= mid and right <= high):
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left+=1
        else:
            temp.append(arr[right])
            right+=1
    while left <= mid:
        temp.append(arr[left])
        left+=1
    while right <= high:
        temp.append(arr[right])
        right+=1
    for i in range(low, high+1):
        arr[i] = temp[i-low]


def mergeSort(arr, low, high):
    if (low >= high):
        return
    mid = (low+high) // 2
    mergeSort(arr, low, mid)
    mergeSort(arr, mid+1, high)
    merge(arr, low, mid, high)


if __name__ == '__main__':
    print(f"Before sorting: {arr}\n")
    low, high = 0, len(arr) - 1
    mergeSort(arr, low, high)
    print(f"\nAfter sorting: {arr}")