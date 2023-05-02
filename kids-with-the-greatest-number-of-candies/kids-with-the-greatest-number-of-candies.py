class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

        m = max(candies)
        r = [False] * len(candies)
        for i in range(len(candies)):
            candy = candies[i] # current have
            
            if (candy + extraCandies >= m):
                r[i] = True

            
        return r

