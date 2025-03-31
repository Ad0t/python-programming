arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

x = int(input("Enter number to be searched: "))

def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            print(f"{x} found at {i}")

linear_search(arr, x)