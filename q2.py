from abc import ABC
from typing import Callable


class OutputType(ABC):
    @classmethod
    def extract_output(cls, lst):
        raise NotImplementedError


class PrintAll(OutputType):
    @classmethod
    def extract_output(cls, lst):
        return lst


class PrintLast(OutputType):
    @classmethod
    def extract_output(cls, lst):
        return lst[-1] if len(lst) > 0 else lst[0]


def search(algorithm: Callable, lst: list, outputtype: OutputType = PrintLast):
    """
    Searchin a list or dict using either bubble sort or selection sort print only the sesult or the output after each
    swap that has been done on the datatype.

    >>> search(algorithm=bubble_sort, lst=[5, 2, 7, 3, 8])
    [2, 3, 5, 7, 8]

    >>> search(algorithm=selection_sort, lst=[5, 2, 7, 3, 8])
    [2, 3, 5, 7, 8]

    >>> search(algorithm=bubble_sort, lst=[5, 2, 7, 3, 8], outputtype=PrintAll)
    [[5, 2, 7, 3, 8], [2, 5, 7, 3, 8], [2, 5, 3, 7, 8], [2, 3, 5, 7, 8]]

    >>> search(algorithm=selection_sort, lst=[5, 2, 7, 3, 8], outputtype=PrintAll)
    [[5, 2, 7, 3, 8], [2, 5, 7, 3, 8], [2, 3, 7, 5, 8], [2, 3, 5, 7, 8]]

    >>> search(algorithm=bubble_sort,lst={'d': 5, 'b': 2, 'e': 7, 'a': 3, 'c': 8})
    ['a', 'b', 'c', 'd', 'e']

    >>> search(algorithm=selection_sort, lst={'d': 5, 'b': 2, 'e': 7, 'a': 3, 'c': 8})
    ['a', 'b', 'c', 'd', 'e']

    >>> search(algorithm=bubble_sort, lst={'d': 5, 'b': 2, 'e': 7, 'a': 3, 'c': 8}, outputtype=PrintAll)
    [['d', 'b', 'e', 'a', 'c'], ['b', 'd', 'e', 'a', 'c'], ['b', 'd', 'a', 'e', 'c'], ['b', 'd', 'a', 'c', 'e'], ['b', 'a', 'd', 'c', 'e'], ['b', 'a', 'c', 'd', 'e'], ['a', 'b', 'c', 'd', 'e']]

    >>> search(algorithm=selection_sort, lst={'d': 5, 'b': 2, 'e': 7, 'a': 3, 'c': 8}, outputtype=PrintAll)
    [['d', 'b', 'e', 'a', 'c'], ['a', 'b', 'e', 'd', 'c'], ['a', 'b', 'c', 'd', 'e']]
    """
    if isinstance(lst, dict):  # items is a dict mapping an item to its value.
        item_names = []
        for key in lst.keys():
            item_names.append(key)
    else:  # items is a list
        item_names = lst
    res = algorithm(item_names)
    return outputtype.extract_output(res)


def bubble_sort(lst):
    """
    >>> bubble_sort([3, 6, 1, 8, 2, 4, 9, 0, 12])
    [[3, 6, 1, 8, 2, 4, 9, 0, 12], [3, 1, 6, 8, 2, 4, 9, 0, 12], [3, 1, 6, 2, 8, 4, 9, 0, 12], [3, 1, 6, 2, 4, 8, 9, 0, 12], [3, 1, 6, 2, 4, 8, 0, 9, 12], [1, 3, 6, 2, 4, 8, 0, 9, 12], [1, 3, 2, 6, 4, 8, 0, 9, 12], [1, 3, 2, 4, 6, 8, 0, 9, 12], [1, 3, 2, 4, 6, 0, 8, 9, 12], [1, 2, 3, 4, 6, 0, 8, 9, 12], [1, 2, 3, 4, 0, 6, 8, 9, 12], [1, 2, 3, 0, 4, 6, 8, 9, 12], [1, 2, 0, 3, 4, 6, 8, 9, 12], [1, 0, 2, 3, 4, 6, 8, 9, 12], [0, 1, 2, 3, 4, 6, 8, 9, 12]]
    """
    res = []
    for i in range(len(lst)):
        flag = True
        for j in range(len(lst) - 1 - i):
            if lst[j] > lst[j + 1]:
                flag = False
                temp_lst = []
                for item in lst:
                    temp_lst.append(item)
                res.append(temp_lst)
                swap = lst[j]
                lst[j] = lst[j + 1]
                lst[j + 1] = swap
        if flag:
            res.append(lst)
            return res
    res.append(lst)
    return res


def selection_sort(lst):
    """
    >>> selection_sort([3, 6, 1, 8, 2, 4, 9, 0, 12])
    [[3, 6, 1, 8, 2, 4, 9, 0, 12], [0, 6, 1, 8, 2, 4, 9, 3, 12], [0, 1, 6, 8, 2, 4, 9, 3, 12], [0, 1, 2, 8, 6, 4, 9, 3, 12], [0, 1, 2, 3, 6, 4, 9, 8, 12], [0, 1, 2, 3, 4, 6, 9, 8, 12], [0, 1, 2, 3, 4, 6, 8, 9, 12]]

    """
    res = []
    for i in range(len(lst)):
        min_val = lst[i]
        min_idx = i
        for j in range(i, len(lst)):
            if lst[j] < min_val:
                min_val = lst[j]
                min_idx = j
        if min_idx != i:
            temp_lst = []
            for item in lst:
                temp_lst.append(item)
            res.append(temp_lst)
            swap = lst[i]
            lst[i] = min_val
            lst[min_idx] = swap
    res.append(lst)
    return res


if __name__ == '__main__':
    print(search(algorithm=bubble_sort, lst=[4, -2, 10, 8]))
    print()
    print(search(algorithm=bubble_sort, lst=[4, -2, 10, 8], outputtype=PrintAll))
