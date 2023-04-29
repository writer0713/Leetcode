class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = []
        for idx, num in enumerate(nums):
            ans.insert(idx, nums[nums[idx]])
        return ans