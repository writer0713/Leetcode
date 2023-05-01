class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            target = nums[i]
            for k in range(i + 1, len(nums)):
                another = nums[k]
                if (target == another):
                    count += 1
        
        return count



            