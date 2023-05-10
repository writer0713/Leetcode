class Solution:

    def calc(num: int) -> int:

        if num % 2 == 0:
            return num // 2
        else:
            return num - 1


    def numberOfSteps(self, num: int) -> int:

        count = 0
        while True:

            if num == 0:
                break
            
            if num % 2 == 0:
                num = num // 2
            else:
                num = num - 1

            count += 1
            
        return count
