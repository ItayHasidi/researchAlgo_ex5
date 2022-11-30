def bounded_subsets_doctest(lst: list, c: int):
    """
    helper function for doctesting bounded_subsets()
    """
    for i in bounded_subsets(lst, c):
        print(i)


def bounded_subsets(lst: list, c: int):
    """
    >>> bounded_subsets_doctest([3, 2, 1], 5)
    []
    [1]
    [2]
    [3]
    [1, 2]
    [1, 3]

    >>> bounded_subsets_doctest([3, 2, 1, 4], 5)
    []
    [1]
    [2]
    [3]
    [1, 2]
    [4]
    [1, 3]
    [1, 4]
    [2, 3]

    """
    res = []
    lst = sorted(lst)
    idx = 0
    last_sum = lst[idx]
    yield res
    while last_sum <= c:
        if last_sum in lst and lst.index(last_sum) < len(lst):
            idx = lst.index(last_sum)
            while res:
                res.pop(-1)
        else:
            i = 0
            while i < len(lst) and last_sum - lst[i] in lst and lst[i] != lst[lst.index(last_sum - lst[i])] and lst[i] + lst[lst.index(last_sum - lst[i])] == last_sum:
                while res:
                    res.pop(-1)
                if lst[i] < lst[lst.index(last_sum - lst[i])]:
                    res.append(lst[i])
                    res.append(lst[lst.index(last_sum - lst[i])])
                    yield res
                i += 1
        if idx < len(lst):
            res.append(lst[idx])
            yield res

        if res and 1 < len(lst) and lst[0] + lst[1] == last_sum:
            last_out = res.pop(-1)
            res.append(lst[0])
            res.append(lst[1])
            yield res
        if res and res[-1] - lst[0] in lst and lst[0] != lst[lst.index(res[-1] - lst[0])] and lst.index(res[-1] - lst[0]) < len(lst) and lst[0] + lst[lst.index(res[-1] - lst[0])] == last_sum:
            last_out = res.pop(-1)
            res.append(lst[0])
            res.append(lst[lst.index(last_out - lst[0])])
            yield res
        if len(res) > 1 and lst.index(res[-1]) + 1 < len(lst) and sum(res[:-1]) + lst[lst.index(res[-1]) + 1] == last_sum:
            last_out = res.pop(-1)
            res.append(lst[lst.index(last_out + 1)])
            yield res
        if len(res) > 1 and lst.index(res[-2]) + 2 < len(lst) and lst[lst.index(res[-2]) + 1] + lst[lst.index(res[-2]) + 2] == last_sum:
            res.pop(-1)
            last_out = res.pop(-1)
            res.append(lst[lst.index(last_out + 1)])
            res.append(lst[lst.index(last_out + 2)])
            yield res
        if len(res) > 2 and lst.index(res[-2]) + 2 < len(lst) and sum(res[:-3]) + lst[lst.index(res[-2]) + 1] + lst[lst.index(res[-2]) + 2] == last_sum:
            res.pop(-1)
            res.append(lst[lst.index(res[-1] + 1)])
            res.append(lst[lst.index(res[-1] + 1)])
            yield res
        else:
            last_sum += 1
            idx += 1
            if res:
                res.pop(-1)


if __name__ == '__main__':
    for s in bounded_subsets([1, 2, 3, 5, 4], 5):
        print(s)
