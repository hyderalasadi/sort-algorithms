from random import choice, shuffle


def quick_sort(A, reverse=False):
    """
    recursive implementation of randomized quick sort, performs in-place sorting with O(nlog(n)) time complexity on average and O(1) auxiliary space
    :param a: array of either all numbers or all strings
    :param reverse: descending order, False by default
    :return sorted list
    """

    if len(A) <= 1:
        return A

    # choose random pivot
    ri = choice(range(len(A)))
    pivot = A[ri]
    A[0], A[ri] = A[ri], A[0]

    i = 1  # i is the index of first element of the greater-than-pivot part
    j = 1  # j is just an index to go over all elements of the list except the pivot
    while j < len(A):
        if not reverse:
            if A[j] > pivot:  # use > for ascending
                j += 1  # check next
            else:
                A[i], A[j] = A[j], A[i]  # swap jth element with the first of greater-than-pivot part
                i += 1  # shift i to the right by one
                j += 1  # check next
        else:
            if A[j] < pivot:  # use < for descending
                j += 1  # check next
            else:
                A[i], A[j] = A[j], A[i]  # swap jth element with the first of greater-than-pivot part
                i += 1  # shift i to the right by one
                j += 1  # check next
    A[0], A[i - 1] = A[i - 1], A[0]  # swap pivot with the last of less-than-pivot part (put pivot in correct sequence)
    A[:i - 1] = quick_sort(A[:i - 1], reverse=reverse)  # recursively sort the left side (less-than-pivot part)
    A[i:] = quick_sort(A[i:], reverse=reverse)  # recursively sort the right side (greater-than-pivot part)
    return A


# driver code for testing
if __name__ == "__main__":
    length = 1000  # test list length, virtually, can be any positive integer
    test_list = list(range(length))  # list of unique integers from 0 to length-1
    shuffle(test_list)  # shuffle test list
    quick_sort(test_list, reverse=False)
    desc_test = all(i[0] == i[1] for i in zip(test_list, [j for j in range(length)]))
    quick_sort(test_list, reverse=True)
    asc_test = all(i[0] == i[1] for i in zip(test_list, [j for j in range(length)][::-1]))
    print("Descending test:", "successful" if desc_test else "unsuccessful",
          "\nAscending test:", "successful" if asc_test else "unsuccessful")
