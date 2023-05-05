class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        
        max = 0
        for person in accounts:
            wealth = sum(person)
            if wealth > max:
                max = wealth
        
        return max