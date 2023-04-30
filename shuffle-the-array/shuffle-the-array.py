class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        arr1 = nums[:n]
        arr2 = nums[n:]
        arr = []
        for idx in range(n):
            arr.append(arr1[idx])
            arr.append(arr2[idx])
        return arr