class Solution:
    def subtractProductAndSum(self, n: int) -> int:

        sum = 0
        product = 1

        for x in list(str(n)):
            target = int(x)
            sum += target
            product *= target

        return product - sum