class Solution:
    def balancedStringSplit(self, s: str) -> int:
        cnt = 0
        r = l = 0
        for char in s: # RLRRLLRLRL
            
            if char == 'R':
                r += 1
            elif char == 'L':
                l += 1

            if r == l:
                cnt += 1
                r = l = 0

        return cnt

