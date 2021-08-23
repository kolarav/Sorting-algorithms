# Time : O(N^2)  Space :  O(1) in-place
# The good thing about selection sort is it never makes more than O(N) swaps and can be useful when memory write is a costly operation.

from typing import List


def selection_sorted(nums: List[int]) -> None:

    length = len(nums)
    for i in range(length):
        min_index = i
        for j in range(i+1, length):
            if nums[min_index] > nums[j]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]


numbers = [1, 4, 3, 52, 45, 29, 26, 378, 1]
print('Before sorting : ', numbers)
selection_sorted(numbers)
print('After sorting : ', numbers)
