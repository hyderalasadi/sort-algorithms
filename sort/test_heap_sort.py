from random import shuffle
from sort import heap_sort


# driver code for testing
if __name__ == "__main__":
    length = 1000  # test list length
    test_list_1 = list(range(length))  # list of unique integers from 0 to length-1
    shuffle(test_list_1)  # shuffle test list
    test_list_2 = test_list_1.copy()
    asc_test_list = heap_sort(test_list_1)
    asc_test = asc_test_list == [j for j in range(length)]
    desc_test_list = heap_sort(test_list_2, reverse=True)
    desc_test = desc_test_list == [j for j in range(length)][::-1]
    print("Ascending test:", "OK" if asc_test else "FAILED!",
            "\nDescending test:", "OK" if desc_test else "FAILED!")
