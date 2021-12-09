"""
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.
"""

import itertools
from collections import defaultdict


def four_sum(array, target):
    seen = defaultdict(set)
    for (i, first), (j, second) in itertools.combinations(enumerate(array), 2):
        seen[first + second].add((i, j))

    result = set()
    for key, first_indices in seen.items():
        second_indices = seen.get(target - key, set())
        for p, q in second_indices:
            for i, j in first_indices:
                # Not reusing the same number twice
                if not ({i, j} & {p, q}):
                    indices = tuple(sorted(array[x] for x in (i, j, p, q)))
                    result.add(indices)
    return result


if __name__ == '__main__':
    print(four_sum([2, 2, 2, 2, 2], 8))
