from random import choice


def quick_sort(a, reverse=False):
    """
    Randomized quick sort, performs in-place sorting
    :param a: array of integers
    :param reverse: descending sort, False by default
    :return sorted list
    """

    if len(a) <= 1:
        return a

    # choose random pivot
    ri = choice(range(len(a)))
    pivot = a[ri]
    a[0], a[ri] = a[ri], a[0]

    i = 1  # i is the index of first element of the greater than pivot part
    j = 1  # j is just an index to go over all elements of the list except the pivot
    while j < len(a):
        if not reverse:
            if a[j] > pivot:  # use > for ascending
                j += 1
            else:
                a[i], a[j] = a[j], a[i]  # swap jth element with first of greater than pivot part
                i += 1
                j += 1
        else:
            if a[j] < pivot:  # use < for descending
                j += 1
            else:
                a[i], a[j] = a[j], a[i]  # swap jth element with first of greater than pivot part
                i += 1
                j += 1
    a[0], a[i - 1] = a[i - 1], a[0]  # swap pivot with last of less than pivot part
    a[:i - 1] = quick_sort(a[:i - 1], reverse=reverse)  # recursively sort the left side
    a[i:] = quick_sort(a[i:], reverse=reverse)  # recursively sort the right side
    return a


# driver code (test)
if __name__ == "__main__":
    with open('data.txt', 'r') as f:
        data_list = f.readlines()
    arr = [int(i) for i in data_list]
    quick_sort(arr, reverse=False)
    desc_test = all(i[0] == i[1] for i in zip(arr, [j for j in range(1, 10001)]))
    quick_sort(arr, reverse=True)
    asc_test = all(i[0] == i[1] for i in zip(arr, [j for j in range(10000, 0, -1)]))
    print("Descending test:", "successful" if desc_test else "unsuccessful",
          "\nAscending test:", "successful" if asc_test else "unsuccessful")
