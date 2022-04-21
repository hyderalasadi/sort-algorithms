from random import shuffle


def k_way_merge(A, reverse=False):
    """
    recursive implementation of k-way merge, merges of multiple arrays with O(n*klog(k))
    time complexity and O(n*k) auxiliary space

    Parameters
    ----------
    A : list
        two or more sorted arrays of any length of same data type (numbers or strings)
    reverse : boolean (False by default)
        if True, the algorithm performs descending sort

    Returns
    -------
    one sorted array
    """

    if len(A) == 1:
        return A[0]

    if len(A) == 2:
        L = A[0]
        R = A[1]
        B = [0 for i in range(len(L) + len(R))]
        i = j = k = 0

        if not reverse:  # for ascending sort
            while i < len(L) and j < len(R):
                if L[i] < R[j]:  # use < for ascending
                    B[k] = L[i]
                    i += 1
                else:
                    B[k] = R[j]
                    j += 1
                k += 1

        else:  # for descending sort
            while i < len(L) and j < len(R):
                if L[i] > R[j]:  # use > for descending
                    B[k] = L[i]
                    i += 1
                else:
                    B[k] = R[j]
                    j += 1
                k += 1

        # checking if any element was left
        while i < len(L):
            B[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            B[k] = R[j]
            j += 1
            k += 1
        return B

    if len(A) > 2:
        mid = len(A)//2
        L = k_way_merge(A[:mid], reverse=reverse)  # merge left half
        R = k_way_merge(A[mid:], reverse=reverse)  # merge right half
        return k_way_merge([L, R], reverse=reverse)  # recursively merge left and right halves


# driver test code
if __name__ == "__main__":
    length = 1000  # test list length
    test_list = list(range(length))  # list of unique integers from 0 to length-1
    shuffle(test_list)  # shuffle test list

    list_1, list_2, list_3 = test_list[:length//5], test_list[length//5:length//2],\
                                test_list[length//2:]  # test splits of different length

    asc_list_1, asc_list_2, asc_list_3 = sorted(list_1), sorted(list_2),\
                                            sorted(list_3)  # ascending sort all splits
    asc_test_lists = [asc_list_1, asc_list_2, asc_list_3]
    asc_test_list = k_way_merge(asc_test_lists)
    asc_test = asc_test_list == sorted(test_list)

    desc_list_1, desc_list_2, desc_list_3 = sorted(list_1, reverse=True), sorted(list_2, reverse=True),\
                                                sorted(list_3, reverse=True)  # descending sort all splits
    desc_test_lists = [desc_list_1, desc_list_2, desc_list_3]
    desc_test_list = k_way_merge(desc_test_lists, reverse=True)
    desc_test = desc_test_list == sorted(test_list, reverse=True)

    print("Ascending test:", "OK" if asc_test else "FAILED!",
            "\nDescending test:", "OK" if desc_test else "FAILED!")
