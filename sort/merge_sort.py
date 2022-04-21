from random import shuffle


def merge_sort(A, reverse=False):
    """
    recursive implementation of merge sort, performs sorting with O(nlog(n)) time complexity
    and O(n) auxiliary space

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

    if len(A) > 1:
        mid = len(A)//2  # finding the mid of the array
        L = A[:mid]  # dividing the array elements into 2 halves, left and right
        R = A[mid:]
        merge_sort(L, reverse=reverse)  # sort the left half
        merge_sort(R, reverse=reverse)  # sort the right half

        # merge left and right side after sort
        i = j = k = 0  # i is L index, j is right index, k is A index

        if not reverse:  # for ascending sort
            while i < len(L) and j < len(R):
                if L[i] < R[j]:  # use < for ascending
                    A[k] = L[i]
                    i += 1
                else:
                    A[k] = R[j]
                    j += 1
                k += 1

        else:  # for descending sort
            while i < len(L) and j < len(R):
                if L[i] > R[j]:  # use > for descending
                    A[k] = L[i]
                    i += 1
                else:
                    A[k] = R[j]
                    j += 1
                k += 1

        # checking if any element was left
        while i < len(L):
            A[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            A[k] = R[j]
            j += 1
            k += 1
    return A


# driver code for testing
if __name__ == "__main__":
    length = 1000  # test list length
    test_list = list(range(length))  # list of unique integers from 0 to length-1
    shuffle(test_list)  # shuffle test list
    asc_test_list = merge_sort(test_list)
    asc_test = asc_test_list == [j for j in range(length)]
    desc_test_list = merge_sort(test_list, reverse=True)
    desc_test = desc_test_list == [j for j in range(length)][::-1]
    print("Ascending test:", "OK" if asc_test else "FAILED!",
            "\nDescending test:", "OK" if desc_test else "FAILED!")
