from random import shuffle
from sort import *


# driver code for testing selection sort
if __name__ == "__main__":
    length = 1000  # test list length
    test_list = list(range(length))  # list of unique integers from 0 to length-1
    shuffle(test_list)  # shuffle test list
    asc_test_list = selection_sort(test_list)
    asc_test = asc_test_list == [j for j in range(length)]
    desc_test_list = selection_sort(test_list, reverse=True)
    desc_test = desc_test_list == [j for j in range(length)][::-1]
    print("Selection sort ascending test:", "OK" if asc_test else "FAILED!",
            "\nSelection sort descending test:", "OK" if desc_test else "FAILED!")

# driver code for testing insertion sort
if __name__ == "__main__":
    length = 1000  # test list length
    test_list = list(range(length))  # list of unique integers from 0 to length-1
    shuffle(test_list)  # shuffle test list
    asc_test_list = insertion_sort(test_list)
    asc_test = asc_test_list == [j for j in range(length)]
    desc_test_list = insertion_sort(test_list, reverse=True)
    desc_test = desc_test_list == [j for j in range(length)][::-1]
    print("Insertion sort ascending test:", "OK" if asc_test else "FAILED!",
            "\nInsertion sort descending test:", "OK" if desc_test else "FAILED!")

# driver code for testing bubble sort
if __name__ == "__main__":
    length = 1000  # test list length
    test_list = list(range(length))  # list of unique integers from 0 to length-1
    shuffle(test_list)  # shuffle test list
    asc_test_list = bubble_sort(test_list)
    asc_test = asc_test_list == [j for j in range(length)]
    desc_test_list = bubble_sort(test_list, reverse=True)
    desc_test = desc_test_list == [j for j in range(length)][::-1]
    print("Bubble sort ascending test:", "OK" if asc_test else "FAILED!",
            "\nBubble sort descending test:", "OK" if desc_test else "FAILED!")

# driver code for testing merge sort
if __name__ == "__main__":
    length = 1000  # test list length
    test_list = list(range(length))  # list of unique integers from 0 to length-1
    shuffle(test_list)  # shuffle test list
    asc_test_list = merge_sort(test_list)
    asc_test = asc_test_list == [j for j in range(length)]
    desc_test_list = merge_sort(test_list, reverse=True)
    desc_test = desc_test_list == [j for j in range(length)][::-1]
    print("Merge sort ascending test:", "OK" if asc_test else "FAILED!",
            "\nMerge sort descending test:", "OK" if desc_test else "FAILED!")

# driver test code k-way merge sort
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

    print("k-way merge sort ascending test:", "OK" if asc_test else "FAILED!",
            "\nk-way merge sort descending test:", "OK" if desc_test else "FAILED!")

# driver code for testing quick sort
if __name__ == "__main__":
    length = 1000  # test list length
    test_list = list(range(length))  # list of unique integers from 0 to length-1
    shuffle(test_list)  # shuffle test list
    asc_test_list = quick_sort(test_list)
    asc_test = asc_test_list == [j for j in range(length)]
    desc_test_list = quick_sort(test_list, reverse=True)
    desc_test = desc_test_list == [j for j in range(length)][::-1]
    print("Quick sort ascending test:", "OK" if asc_test else "FAILED!",
            "\nQuick sort descending test:", "OK" if desc_test else "FAILED!")

# driver code for testing heap sort
if __name__ == "__main__":
    length = 1000  # test list length
    test_list_1 = list(range(length))  # list of unique integers from 0 to length-1
    shuffle(test_list_1)  # shuffle test list
    test_list_2 = test_list_1.copy()
    asc_test_list = heap_sort(test_list_1)
    asc_test = asc_test_list == [j for j in range(length)]
    desc_test_list = heap_sort(test_list_2, reverse=True)
    desc_test = desc_test_list == [j for j in range(length)][::-1]
    print("Heap sort ascending test:", "OK" if asc_test else "FAILED!",
            "\nHeap sort descending test:", "OK" if desc_test else "FAILED!")
