#  Bubble sort is a simple sorting , in this case we repeatedly swap two adjacent elements if they are not in order
#  Time : worst case -> O(N^2) best case -> O(N)    Space : O(1) in-place  Stable
# This is an optimized version of bubble sort

from time import time
from typing import List


def bubble_sorted(nums: List[int]) -> None:
    # this method alters the original list
    # If you don't want that just make a copy of the  list with different name and do the process and return at the end
    length = len(nums)
    for i in range(length):
        swapped = False
        for j in range(length-1-i):
            if nums[j] > nums[j+1]:
                nums[j+1], nums[j] = nums[j], nums[j+1]
                swapped = True
        # In case the whole list is already sorted there won't be any swap
        # so it is useless to go through N number of iteration for i
        if (swapped == False):
            break


numbers = [1, 4, 3, 52, 45, 29, 26, 378, 1]
print('Before sorting : ', numbers)
bubble_sorted(numbers)
print('After sorting : ', numbers)
