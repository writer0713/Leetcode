class Solution:
    def minimumSum(self, num: int) -> int:

        arr = sorted([x for x in str(num)])
        first_num = int(arr[0] + arr[2])
        second_num = int(arr[1] + arr[3])

        return first_num + second_num
