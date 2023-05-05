from collections import defaultdict

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        dict = defaultdict(int)

        for idx in range(len(nums)):
            value = nums[idx]

            if idx == 0:
                dict[idx] = value
            else:
                dict[idx] = value + dict[idx - 1]

        print(dict.values())
        
        return dict.values()
            

