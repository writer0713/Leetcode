class Solution:
    def isPalindrome(self, x: int) -> bool:
        target = str(x)
        return target == target[::-1]
        