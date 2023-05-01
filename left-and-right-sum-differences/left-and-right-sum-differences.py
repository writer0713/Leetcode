class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        ls = 0
        rs = sum(nums)
        n = []
        for num in nums:
            rs -= num
            n.append(abs(ls - rs))
            ls += num
        return n


            