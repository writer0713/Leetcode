class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        
        result = [""] * len(s)
        for idx, char in enumerate(s):

            real_idx = indices[idx]
            result[real_idx] = char

        return "".join(result)
