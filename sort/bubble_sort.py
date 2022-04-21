from random import shuffle


def bubble_sort(A, reverse=False):
    """
    performs in-place sorting with O(n^2)) time complexity, with optimized
    implementation O(n) time complexity for best case when the array is already
    sorted, and O(1) auxiliary space

    Parameters
    ----------
    A: list
        array of either all numbers or all strings

    reverse : boolean (False by default)
        if True, the algorithm performs descending sort

    Returns
    -------
    sorted array
    """

    n = len(A)
    # loop over the array n-1 times, the nth loop is redundant because
    # the smallest element (for ascending) will be already in the first
    # position, as all bigger (for ascending) elements bubbled to the end
    for i in range(n-1):
        swapped = False
        # loop over the needed number of comparisons
        # to reach the last unsorted element in the array
        for j in range(0, n-1-i):
            if not reverse:
                if A[j] > A[j+1]:  #use > for ascending
                    A[j], A[j+1] = A[j+1], A[j]
                    swapped = True
            else:
                if A[j] < A[j+1]:  #use < for descending
                    A[j], A[j+1] = A[j+1], A[j]
                    swapped = True
        # if no two elements were swapped by inner loop, then
        # array is already sorted at this stage, break outer loop
        if swapped == False:
            break
    return A


# driver code for testing
if __name__ == "__main__":
    length = 1000  # test list length
    test_list = list(range(length))  # list of unique integers from 0 to length-1
    shuffle(test_list)  # shuffle test list
    asc_test_list = bubble_sort(test_list)
    asc_test = asc_test_list == [j for j in range(length)]
    desc_test_list = bubble_sort(test_list, reverse=True)
    desc_test = desc_test_list == [j for j in range(length)][::-1]
    print("Ascending test:", "OK" if asc_test else "FAILED!",
            "\nDescending test:", "OK" if desc_test else "FAILED!")
