class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        result = 0
        for op in operations:
            if "++" in op:
                result += 1
            else:
                result -= 1
        return result