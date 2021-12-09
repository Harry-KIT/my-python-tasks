"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""

from typing import List


def twosum_indices_linear(nums: List[int], target: int) -> tuple[int, ...]:
    numtoindexmap = {}
    for num1_index, num1 in enumerate(nums):
        num2 = target - num1
        try:
            num2_index = numtoindexmap[num2]
        except KeyError:
            numtoindexmap[num1] = num1_index
        else:
            return tuple(sorted([num1_index, num2_index]))


if __name__ == '__main__':
    print(twosum_indices_linear([2, 7, 11, 15], 9))


