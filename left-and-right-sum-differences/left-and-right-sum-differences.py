class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        answer = []
        for i in range(len(nums)):
            l = 0
            r = 0
            # leftsum
            if i == 0:
                l = 0
            else:
                l = sum(nums[:i])
            
            # rightsum
            if i == len(nums) - 1:
                r = 0
            else:
                r = sum(nums[i+1:])
            
            answer.append(abs(l - r))
        
        return answer