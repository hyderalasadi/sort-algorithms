from random import choice
import heapq as hq

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

def bubble_sort(A, reverse=False):
    """
    performs in-place sorting with O(n^2)) time complexity, with optimized
    implementation O(n) time complexity for best case when the array is already
    sorted, and O(1) auxiliary space

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

    n = len(A)
    # loop over the array n-1 times, the nth loop is redundant because
    # the smallest element (for ascending) will be already in the first
    # position, as all bigger (for ascending) elements bubbled to the end
    for i in range(n-1):
        swapped = False
        # loop over the needed number of comparisons
        # to reach the last unsorted element in the array
        for j in range(0, n-1-i):
            if not reverse:
                if A[j] > A[j+1]:  #use > for ascending
                    A[j], A[j+1] = A[j+1], A[j]
                    swapped = True
            else:
                if A[j] < A[j+1]:  #use < for descending
                    A[j], A[j+1] = A[j+1], A[j]
                    swapped = True
        # if no two elements were swapped by inner loop, then
        # array is already sorted at this stage, break outer loop
        if swapped == False:
            break
    return A

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

def quick_sort(A, reverse=False):
    """
    recursive implementation of randomized quick sort, performs in-place sorting
    with O(nlog(n)) time complexity on average and O(1) auxiliary space

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

def heap_sort(A, reverse=False):
    """
    performs sorting using heapq module with O(nlogn)) time complexity and O(n) auxiliary space

    Parameters
    ----------
    A: list
        array of numbers

    reverse : boolean (False by default)
        if True, the algorithm performs descending sort

    Returns
    -------
    sorted array
    """
    n = len(A)
    if not reverse:
        hq.heapify(A)
        B = []
        for i in range(n):
            B.append(hq.heappop(A))
    else:
        A = [-i for i in A]
        hq.heapify(A)
        B = []
        for i in range(n):
            B.append(hq.heappop(A) * -1)
    return B
