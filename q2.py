

class bounded_subsets:
    def __init__(self, s, c):
        self.s = sorted(s)
        self.c = c
        self.state = []
        self.is_first = True

    def __iter__(self):
        return self

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
            if len(self.state) > 0 and self.state[-1] == self.s[-1] or sum(self.state) == self.c:
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


if __name__ == '__main__':
    for s in bounded_subsets([1, 2, 3], 4):
        print(s)  # prints: [], [1], [2], [3], [1,2], [1,3].
    print()
    for s in bounded_subsets(range(50, 150), 103):
        print(s)  # prints: [], [50], [51],..., [103], [50, 51], [50, 52], [50, 53], [51, 52]
    print()
    for s in zip(range(5), bounded_subsets(range(100), 1000000000000)):
        print(s)  # prints: (0,[]), (1,[0]), (2,[1]), (3,[2]), (4,[3]