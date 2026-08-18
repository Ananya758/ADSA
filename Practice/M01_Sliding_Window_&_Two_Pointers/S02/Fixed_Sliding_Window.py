'''
643. Maximum Average Subarray I
1343. Number of subarrays of size k and average greater than or equal to threshold
1456. 
'''

# Maximum Average Subarray I (Traditional approach)
from typing import List
def findMaxAverage(nums: List[int], k: int) -> float:
    max_sum = float("-inf")
    n = len(nums)
    for i in range(n - k + 1):
        sub_sum = 0
        for j in range(i, k + i):
            sub_sum += nums[j]
        max_sum = max(max_sum, sub_sum)
    return max_sum/k
nums = [1,12,-5,-6,50,3]
k = 4
print(findMaxAverage(nums,k))
# MAS ---> in optimal approach
def findMaxAverage_Optimal(nums: List[int], k: int) -> float:
        win_sum = sum(nums[:k])
        max_sum = win_sum
        n = len(nums)
        for i in range(0, n - k):
            win_sum = win_sum - nums[i] + nums[k + i]
            max_sum = max(win_sum, max_sum)
        return max_sum/k
nums = [1,12,-5,-6,50,3]
k = 4
print(findMaxAverage_Optimal(nums,k))

# Number of subarrays of size k and average greater than or equal to threshold
def numOfSubarrays(arr: List[int], k: int, threshold: int) -> int:
    count = 0
    n = len(arr)
    win_sum = sum(arr[:k])
    if (win_sum/k) >= threshold:
        count += 1
    for i in range(0, n - k):
        win_sum = win_sum - arr[i] + arr[k + i]
        if (win_sum/k) <= threshold:
            count += 1
    return count 
arr = [2,2,2,2,5,5,5,8]
k = 3
threshold = 4
print(numOfSubarrays(arr, k, threshold))
        
