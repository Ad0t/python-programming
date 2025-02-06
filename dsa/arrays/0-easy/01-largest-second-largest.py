def findlargest (arr):
    largest = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > largest:
            largest = arr[i]
    return largest

def findlargest2 (arr):
    largest, largest2 = arr[0], -1
    for i in range(1, len(arr)):
        if arr[i] > largest:
            largest2 = largest
            largest = arr[i]
        elif arr[i] > largest2 and arr[i] < largest:
            largest2 = arr[i]
    return largest2


def findsmallest (arr):
    smallest = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
    return smallest

def findsmallest2 (arr):
    smallest, smallest2 = arr[0], findlargest(arr)
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest2 = smallest
            smallest = arr[i]
        elif arr[i] < smallest2 and arr[i] > smallest:
            smallest2 = arr[i]
    return smallest2



if __name__ == '__main__':
    arr = [12, 45, 7, 23, 56, 89]
    print(arr)
    print(f"Largest element is {findlargest(arr)}")
    print(f"Second largest element is {findlargest2(arr)}")
    print(f"Smallest element is {findsmallest(arr)}")
    print(f"Second smallest element is {findsmallest2(arr)}")
