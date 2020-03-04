# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        smallest_index = i
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for e in range(i + 1, len(arr)):
            if arr[e] < arr[smallest_index]:
                smallest_index = e

        # TO-DO: swap
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # number of iterations for range
    iter = len(arr)
    # starting from the secon number
    for i in range(1, iter):
        # starting from the first number
        for j in range(0, iter - 1):
            # if the second number (i) is smaller then first number (j)
            if arr[i] < arr[j]:
                # swap
                arr[j], arr[i] = arr[i], arr[j]
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr