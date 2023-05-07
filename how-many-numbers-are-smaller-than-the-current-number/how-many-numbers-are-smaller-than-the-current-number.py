class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        map = {}
        temp = sorted(nums) # ex) 1, 2, 2, 3, 8

        for i, num in enumerate(temp):
            if num not in map: # {1: 0, 2: 1, 3: 3, 8: 4}
                map[num] = i

        print(map)

        return [map[num] for num in nums]



