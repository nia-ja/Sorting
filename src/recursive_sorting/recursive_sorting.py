# TO-DO: complete the helpe function below to merge 2 sorted arrays
# given two sorted arrays, return a new combined array
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [] * elements
    # TO-DO
    i = 0
    j = 0
    while i < len(arrA) and j < len(arrB):
        #compare the two values, choose the smaller one
        if (arrA[i] <= arrB[j]):
            merged_arr.append(arrA[i])
            i+=1
        else:
            merged_arr.append(arrB[j])
            j+=1
    
    return merged_arr + arrA[i:] + arrB[j:]

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    # base case
    if len(arr) <= 1:
        return arr

    #divide the arrays
    half = len(arr) // 2 # round down
    left = merge_sort(arr[:half]) # call same function on result while base case is not reached
    right = merge_sort(arr[half:])

    #merging sorted arrays
    arr = merge(left, right)

    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
