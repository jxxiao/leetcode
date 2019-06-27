class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1, num2, l1, l2 = num1[::-1], num2[::-1], len(num1), len(num2)
        carry, start = 0, 0
        ans = [0] * (l1 + l2)
        for i in range(l1):
            for j in range(l2):
                ans[i + j] += int(num1[i]) * int(num2[j])
        for i in range(len(ans)):
            ans[i], carry = (ans[i] + carry) % 10, int((ans[i] + carry) / 10)
        ans = map(str, ans)
        answer = ''.join(ans)[::-1]
        while start < len(answer) and answer[start] == '0':
            start += 1
        return answer[start:] if start != len(answer) else '0'


print(Solution().multiply('28', '26'))
