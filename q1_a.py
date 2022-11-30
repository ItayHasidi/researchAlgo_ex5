def bounded_subsets_doctest(lst: list, c: int):
    """
    helper function for doctesting bounded_subsets()
    """
    for i in bounded_subsets(lst, c):
        print(i)


def bounded_subsets(lst: list, c: int):
    """
    Making an iterator style function using generator

    >>> bounded_subsets_doctest([2,5,8,1], 10)
    []
    [1]
    [2]
    [5]
    [8]
    [1, 2]
    [1, 5]
    [1, 8]
    [2, 5]
    [2, 8]

    >>> bounded_subsets_doctest([2,4,3,1], 8)
    []
    [1]
    [2]
    [3]
    [4]
    [1, 2]
    [1, 3]
    [1, 4]
    [2, 3]
    [2, 4]
    [3, 4]
    [1, 2, 3]
    [1, 2, 4]
    [1, 3, 4]

    """
    res = []
    lst = sorted(lst)
    idx = 0
    yield res
    while sum(res) <= c:
        if idx < len(lst):
            res.append(lst[idx])
            if sum(res) <= c:
                yield res
            if res:
                last_out = res.pop(-1)
                idx = lst.index(last_out) + 1
        if idx == len(lst):
            if not res and len(lst) > 0:
                res.append(lst[0])
                res.append(lst[1])
                idx = 2
                if sum(res) <= c:
                    yield res
                    res.pop(-1)
            elif res and len(lst) - lst.index(res[-1]) == 2:
                res.pop(-1)
                if not res:
                    res.append(lst[0])
                    res.append(lst[1])
                    idx = 2
                else:
                    res.append(lst[lst.index(res[-1]) + 1])
                    res.append(lst[lst.index(res[-1]) + 1])
                    idx = lst.index(res[-1]) + 1
            elif res and len(lst) - lst.index(res[-1]) > 1:
                last_out = res.pop(-1)
                res.append(lst[lst.index(last_out) + 1])
                res.append(lst[lst.index(last_out) + 2])
                idx = lst.index(res[-1]) + 1
                if sum(res) <= c:
                    yield res
                    res.pop(-1)


if __name__ == '__main__':
    for s in bounded_subsets([1, 2, 3, 5, 4], 7):
        print(s)  # prints: [], [1], [2], [3], [1,2], [1,3].
    print()
    for s in bounded_subsets(range(50, 150), 103):
        print(s)  # prints: [], [50], [51],..., [103], [50, 51], [50, 52], [50, 53], [51, 52]
    print()
    for s in zip(range(5), bounded_subsets(range(100), 1000000000000)):
        print(s)  # prints: (0,[]), (1,[0]), (2,[1]), (3,[2]), (4,[3])
