from random import shuffle
from sort import k_way_merge


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
