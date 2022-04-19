from random import shuffle


def k_way_merge(A, reverse=False):
    """
    recursive implementation of k-way merge, merges of multiple arrays with O(n*klog(k))
    time complexity and O(n*k) auxiliary space
    :param A: list of sorted arrays of any length of either all numbers or all strings
    :param reverse: descending order, False by default
    :return one sorted array
    """

    if len(A) == 1:
        return A[0]

    if len(A) == 2:
        L = A[0]
        R = A[1]
        O = [0 for i in range(len(L) + len(R))]
        i = j = k = 0

        if not reverse:  # for ascending sort
            while i < len(L) and j < len(R):
                if L[i] < R[j]:  # use < for ascending
                    O[k] = L[i]
                    i += 1
                else:
                    O[k] = R[j]
                    j += 1
                k += 1

        else:  # for descending sort
            while i < len(L) and j < len(R):
                if L[i] > R[j]:  # use > for descending
                    O[k] = L[i]
                    i += 1
                else:
                    O[k] = R[j]
                    j += 1
                k += 1

        # checking if any element was left
        while i < len(L):
            O[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            O[k] = R[j]
            j += 1
            k += 1
        return O

    if len(A) > 2:
        mid = len(A)//2
        L = k_way_merge(A[:mid], reverse=reverse)  # merge left half
        R = k_way_merge(A[mid:], reverse=reverse)  # merge right half
        return k_way_merge([L, R], reverse=reverse)  # recursively merge left and right halves


# driver code for testing
if __name__ == "__main__":
    length = 100000  # test list length, virtually, can be any positive integer
    test_list = list(range(length))  # list of unique integers from 0 to length-1
    shuffle(test_list)  # shuffle test list
    list_1, list_2, list_3 = test_list[:length//5], test_list[length//5:length//2],\
                                test_list[length//2:]  # split test list

    asc_list_1, asc_list_2, asc_list_3 = sorted(list_1), sorted(list_2), sorted(list_3)  # ascending sort all splits
    asc_test_lists = [asc_list_1, asc_list_2, asc_list_3]  # put sorted lists in one big ascending sort list
    asc_test_list = k_way_merge(asc_test_lists, reverse=False)
    asc_test = all(i[0] == i[1] for i in zip(asc_test_list, [j for j in range(length)]))

    desc_list_1, desc_list_2, desc_list_3 = sorted(list_1, reverse=True), sorted(list_2, reverse=True),\
                                                sorted(list_3, reverse=True)  # descending sort all splits
    desc_test_lists = [desc_list_1, desc_list_2, desc_list_3]  # put sorted lists in one big descending sort list
    desc_test_list = k_way_merge(desc_test_lists, reverse=True)
    desc_test = all(i[0] == i[1] for i in zip(desc_test_list, [j for j in range(length)][::-1]))

    print("Descending test:", "successful" if desc_test else "unsuccessful",
            "\nAscending test:", "successful" if asc_test else "unsuccessful")
