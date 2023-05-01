class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        leftSum = []
        rightSum = []
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

            # # leftsum
            # if i == 0:
            #     leftSum.append(0)
            # else:
            #     leftSum.append(sum(nums[:i]))
            
            # # rightsum
            # if i == len(nums) - 1:
            #     rightSum.append(0)
            # else:
            #     rightSum.append(sum(nums[i+1:]))
        
        # answer = []
        # for i in range(len(nums)):
        #     left = leftSum[i]
        #     right = rightSum[i]
        #     answer.append(abs(left - right))
        
        # return answer