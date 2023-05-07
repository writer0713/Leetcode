class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        result = [0] * len(nums)

        for idx, target in enumerate(nums):
            for k in range(len(nums)):
                if nums[k] < target:
                    result[idx] += 1

        return result



