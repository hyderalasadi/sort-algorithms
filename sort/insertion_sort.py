from random import shuffle


def insertion_sort(A, reverse=False):
    """
    performs in-place sorting with O(n^2)) time complexity and O(1) auxiliary space

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

    for i in range(1, len(A)):  # loop over all elemets starting from the second element
        key = A[i]  # key is the element to be processed, initiated as the second element
        j = i-1  # j is the index of the biggest/smallest sorted element, initiated as the frist element
        if not reverse:
            while j >= 0 and key < A[j]:  # if key is smaller than largest sorted element
            	A[j + 1] = A[j]  # shift largest sorted elements to the right
            	# compare the next largest until key is no longer smaller
            	# or no more element to compare to (smaller than first element)
            	j -= 1
        else:
            while j >= 0 and key > A[j]:  # if key is bigger than smallest sorted element
            	A[j + 1] = A[j]  # shift smallest sorted elements to the right
            	# compare the next largest until key is no longer smaller
            	# or no more element to compare to (smaller than first element)
            	j -= 1
        A[j + 1] = key  # insert key in its correct place
    return A


# driver code for testing
if __name__ == "__main__":
    length = 1000  # test list length
    test_list = list(range(length))  # list of unique integers from 0 to length-1
    shuffle(test_list)  # shuffle test list
    asc_test_list = insertion_sort(test_list)
    asc_test = asc_test_list == [j for j in range(length)]
    desc_test_list = insertion_sort(test_list, reverse=True)
    desc_test = desc_test_list == [j for j in range(length)][::-1]
    print("Ascending test:", "OK" if asc_test else "FAILED!",
            "\nDescending test:", "OK" if desc_test else "FAILED!")
