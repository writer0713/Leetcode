class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        l = set(jewels)
        c = 0
        for stone in stones:
            if stone in l:
                c += 1
        return c
