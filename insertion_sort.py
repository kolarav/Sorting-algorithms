# In this case we starts from position one and go all the way to the end of the list
# check if previous element is greater than key until the start and then swap accordingly
# Time : best case -> O(N) worst case -> O(N^2)  Space : O(1) in-place  Stable

# Insertion sort is used when number of elements is small.
#  It can also be useful when input array is almost sorted, only few elements are misplaced in complete big array.

from typing import List


def insertion_sorted(nums: List[int]) -> None:
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1
        while (nums[j] > key and j >= 0):
            nums[j + 1] = nums[j]
            j = j - 1
        nums[j + 1] = key


numbers = [1, 4, 3, 52, 45, 29, 26, 378, 1]
print('Before sorting : ', numbers)
insertion_sorted(numbers)
print('After sorting : ', numbers)
