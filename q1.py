def is_less(lst1, lst2):
    """
    if lst1 is less of value at a specific index than lst2 at the same index - returns true
    """
    is_last = False
    if len(lst1) != len(lst2):
        return False
    for i in range(len(lst1)):
        if lst1[i] < lst2[i] and i + 1 < len(lst1):
            i = i - 1
            if i < 0:
                i = 0
                is_last = True
            return False, is_last, i
        # elif lst1[i] >= lst2[i] and i + 1 == len(lst1):
        #     return False
    return True, is_last, -1


def next_helper(state):
    


class bounded_subsets:
    def __init__(self, s, c):
        self.s = sorted(s)
        self.c = c
        self.state = []
        self.is_first = True

    def __iter__(self):
        return self

    def __next__(self):
        last_state = []
        last_good_state = []
        last_not_good_1 = False
        last_not_good_2 = False
        is_last = False
        for obj in self.state:
            last_state.append(obj)
            last_good_state.append(obj)
        length = len(self.s)
        if sum(self.state) > self.c:
            raise StopIteration
        if self.is_first:
            self.is_first = False
            return self.state
        while True:
            if not self.state:
                idx = 0
            else:
                idx = self.s.index(self.state[-1]) + 1
            if idx < length and self.s[idx] <= self.c:
                if self.state:
                    self.state.pop(-1)
                self.state.append(self.s[idx])
                if sum(self.state) <= self.c and len(last_state) <= len(self.state):
                    if last_good_state != self.state and not last_not_good_2:
                        for obj in self.state:
                            last_good_state.append(obj)
                        return self.state
                    else:
                        raise StopIteration
                else:
                    flag, is_last, i = is_less(last_state, self.state)
                    last_state = []
                    for obj in self.state:
                        last_state.append(obj)
                    if not flag:
                        range_itr = len(self.state) - i
                        for j in range(range_itr):
                            self.state.pop(-1)
                        if self.state:
                            idx = self.s.index(self.state[-1]) + 1
                        else:
                            if not is_last:
                                idx = self.s.index(last_state[0]) + 1
                            else:
                                idx = 0
                        self.state.append(self.s[idx])
                        self.state.append(self.s[idx])
                        self.state.append(self.s[idx])
                        if not last_not_good_1:
                            last_not_good_1 = True
                        elif last_not_good_1 and not last_not_good_2:
                            last_not_good_2 = True
            if self.state:
                self.state.pop(-1)
                if not self.state:
                    idx = 0
                else:
                    idx = self.s.index(self.state[-1]) + 1
                if idx < length:
                    if self.state:
                        self.state.pop(-1)
                    self.state.append(self.s[idx])
                    self.state.append(self.s[idx])



"""
    def __next__(self):
        if sum(self.state) > self.c:
            raise StopIteration
        if self.is_first:
            self.is_first = False
            return self.state
        while sum(self.state) <= self.c:
            if len(self.state) != 0:
                res = self.state[-1]
                next_idx = self.s.index(res) + 1
            else:
                next_idx = 0
            if (len(self.state) == 1 and self.state[-1] == self.s[-1]) or sum(self.state) == self.c:
                self.state.pop(-1)
                if len(self.state) == 0:
                    next_idx = 0
                else:
                    res = self.state[-1]
                    next_idx = self.s.index(res) + 1
                if next_idx + 1 < len(self.s) and self.s[next_idx] + self.s[next_idx + 1] <= self.c\
                        and len(self.state) > 0:
                    self.state.pop(-1)
                self.state.append(self.s[next_idx])
                self.state.append(self.s[next_idx + 1])
                if sum(self.state) <= self.c:
                    return self.state
                else:
                    raise StopIteration

            if next_idx < len(self.s) and sum(self.state[:-1]) + self.s[next_idx] <= self.c:
                if len(self.state) != 0:
                    self.state.pop(-1)
                self.state.append(self.s[next_idx])
                return self.state
"""

if __name__ == '__main__':
    for s in bounded_subsets([1, 2, 3, 5, 4], 9):
        print(s)  # prints: [], [1], [2], [3], [1,2], [1,3].
    print()
    # for s in bounded_subsets(range(50, 150), 103):
    #     print(s)  # prints: [], [50], [51],..., [103], [50, 51], [50, 52], [50, 53], [51, 52]
    # print()
    # for s in zip(range(5), bounded_subsets(range(100), 1000000000000)):
    #     print(s)  # prints: (0,[]), (1,[0]), (2,[1]), (3,[2]), (4,[3]
