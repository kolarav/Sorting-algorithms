# Time : O(Nlog N)  Space : O(N) not   in-place   Stable
# Drawbacks ->
#  Merge sort algorithm requires an additional memory space of 0(n) for the temporary array.
#  It goes through the whole process even if the array is sorted.
# It is useful for linked list as we do not need to assign any new space for the elements, we can just alter the their next pointer. so Space becomes O(1)

def merge_sorted(nums):
    if len(nums) > 1:

        mid = len(nums)//2

        left = nums[:mid]
        right = nums[mid:]

        merge_sorted(left)
        merge_sorted(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1


numbers = [5, 4, 3, 2, 1]
print('Before sorting : ', numbers)
merge_sorted(numbers)
print('After sorting : ', numbers)
