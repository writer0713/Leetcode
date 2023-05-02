class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        m = max(candies)
        return [True if candy + extraCandies >= m else False for candy in candies]
        

