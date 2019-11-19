class Solution:
    def getPermutation(self, n, k):
        nums = list(range(1, n+1))
        length = len(nums)
        result = ""
        while length > 1:
            fact = math.factorial(length-1)
            index = (k-1)//fact
            num = nums[index]
            result += str(num)
            nums.remove(num)
            length = len(nums)
            k = k - index*fact
        result += str(nums[0])
        return result