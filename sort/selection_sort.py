from random import shuffle


def selection_sort(A, reverse=False):
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

    for i in range(len(A)):
        if not reverse:  # find the index of the smallest element in remaining unsorted array
            min_idx = i
            for j in range(i+1, len(A)):
                if A[min_idx] > A[j]:  # use > for ascending
                    min_idx = j
            A[i], A[min_idx] = A[min_idx], A[i]  # swap the smallest element with the first element
        else:  # find the index of the biggest element in remaining unsorted array
            max_idx = i
            for j in range(i+1, len(A)):
                if A[max_idx] < A[j]:  # use < for descending
                    max_idx = j
            A[i], A[max_idx] = A[max_idx], A[i]  # swap the biggest element with the first element
    return A


# driver code for testing
if __name__ == "__main__":
    length = 1000  # test list length
    test_list = list(range(length))  # list of unique integers from 0 to length-1
    shuffle(test_list)  # shuffle test list
    asc_test_list = selection_sort(test_list)
    asc_test = asc_test_list == [j for j in range(length)]
    desc_test_list = selection_sort(test_list, reverse=True)
    desc_test = desc_test_list == [j for j in range(length)][::-1]
    print("Ascending test:", "OK" if asc_test else "FAILED!",
            "\nDescending test:", "OK" if desc_test else "FAILED!")
