from typing import List
def twoSum(nums: List[int], target: int) -> List[int]:
    arr = {}
    for i, num in enumerate(nums):
        cp = target - num
        if cp in arr:
            return [arr[cp], i]
        arr[num] = i
