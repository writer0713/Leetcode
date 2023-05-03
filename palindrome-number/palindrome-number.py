from collections import deque

class Solution:
    def isPalindrome(self, x: int) -> bool:
        dq = deque(list(str(x)))
        while len(dq) > 1:
            left = dq.popleft()
            right = dq.pop()
            if left != right:
                return False
        
        return True
        