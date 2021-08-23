# Quick sort uses Divide and Counqure method to do the soting
# Time : O(Nlog N) space : O(1)   in-place  unstable by default but can be made stable
# Quick sort has auxilary space advantage over merge sort thats why it is preferred


from typing import List


#  This is to get the median of the values
#  This is just returning the value which is closer to the average of these three values among themselves.
def median(a, b, c):
    if (a - b) * (c - a) >= 0:
        return a
    elif (b - a) * (c - b) >= 0:
        return b
    else:
        return c


def partition(nums: List[int], start: int, end: int) -> int:

    a = nums[start]
    b = nums[end]
    c = (end+start)//2
    pivot = median(a, b, c)
    p_idx = nums.index(pivot)
    nums[p_idx], nums[end] = nums[end], pivot
    # Above part is done to optimize the quick sort even if we don't do all that quick sort will still work but will be little slower.

    pivot = nums[end]
    p_idx = start
    for idx in range(start, end):
        if nums[idx] <= pivot:
            nums[p_idx], nums[idx] = nums[idx], nums[p_idx]
            p_idx += 1
    nums[p_idx], nums[end] = nums[end], nums[p_idx]

    return p_idx


def quick_sorted(nums: List[int], start: int, end: int) -> None:
    if(start < end):
        p_idx = partition(nums, start, end)
        quick_sorted(nums, start, p_idx-1)
        quick_sorted(nums, p_idx+1, end)


numbers = [9, 8, 7, 6, 4, 5, 5, 4, 3, 2, 1, 0]
quick_sorted(numbers, start=0, end=len(numbers)-1)
print(numbers)
