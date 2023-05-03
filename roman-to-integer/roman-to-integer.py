class Solution:
    def romanToInt(self, romans: str) -> int:

        romanIntegers = { 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000 }
        result = 0
        
        for idx in range(1, len(romans)):
            first = romanIntegers[romans[idx - 1]]
            second = romanIntegers[romans[idx]]

            if (first < second):
                result -= first
            else:
                result += first

        result += romanIntegers[romans[-1]]
        
        return result
            