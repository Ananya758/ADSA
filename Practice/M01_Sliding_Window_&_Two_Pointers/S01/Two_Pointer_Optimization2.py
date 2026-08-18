'''
26. Remove Duplicates form sorted array
27. Remove Element
283. Move Zeros
167. Two Sum ll - Input array is sorted 
977. Squares of a sorted array
'''


# Remove Duplicates form sorted array
from typing import List
def removeDuplicates(nums: List[int]) -> int:
    i = 0
    for j in range(1, len(nums)):
        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]
    return i + 1
nums = [0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates(nums))

# Remove Element
def removeElement(nums: List[int], val: int) -> int:
    i = 0
    for j in range(0, len(nums)):
        if nums[j] != val:
            nums[i] = nums[j]
            i += 1
    return i
nums = [0,1,2,2,3,0,4,2]
val = 2
print(removeElement(nums, val))

# Two Sum ll - Input array is sorted 
def twoSum(numbers: List[int], target: int) -> List[int]:
    n = len(numbers)
    left = 0
    right = n - 1
    while left < right:
        s = numbers[left] + numbers[right]
        if s == target:
            return [left + 1, right + 1]
        elif s > target:
            right -= 1
        else:
            left += 1
numbers = [2,7,11,15]
target = 9
print(twoSum(numbers, target))

# Squares of a sorted array
def sortedSquares(nums: List[int]) -> List[int]:
        res = [ele**2 for ele in nums] #O(n)
        res.sort() #O(nlogn)
        return res
nums = [-4,-1,0,3,10]
print(sortedSquares(nums))
