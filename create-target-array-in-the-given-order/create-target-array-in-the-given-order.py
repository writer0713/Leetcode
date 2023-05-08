class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:

        result = []


        for i in range(len(nums)):
            idx = index[i]
            result.insert(idx, nums[i])

        return result