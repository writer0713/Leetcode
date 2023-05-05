class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        
        max_wealth = 0
        for person in accounts:
            max_wealth = max(max_wealth, sum(person))
        
        return max_wealth