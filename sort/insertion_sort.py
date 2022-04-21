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

    # i is the index of the element to be processed, starts from the 2nd element
    for i in range(1, len(A)):
        key = A[i]  # key is the value of the element being processed, initiated as the 2nd element value
        j = i - 1  # j is the index of the biggest(ascending)/smallest(descending) sorted element,
                 # initiated as the 1st element
        if not reverse:
            while j >= 0 and key < A[j]:  # if key is smaller than sorted elements
            	A[j + 1] = A[j]  # shift bigger sorted element 1 position to the right
            	# compare next smaller sorted element (left) until key is no longer
			    # smaller or no more elements to compare to (smaller than 1st element)
            	j -= 1
        else:
            while j >= 0 and key > A[j]:  # if key is larger than sorted elements
            	A[j + 1] = A[j]  # shift smaller sorted element 1 position to the right
            	# compare next bigger sorted element (left) until key is no longer
			    # bigger or no more elements to compare to (bigger than 1st element)
            	j -= 1
        # insert key in its correct place, just before the last bigger(ascending)/smaller(descending)
		# sorted element, this position should be empty due to shifting
        A[j + 1] = key
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
