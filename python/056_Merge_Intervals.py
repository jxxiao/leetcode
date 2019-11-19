class Solution:
    def merge(self, intervals):
        out = []
        for i in sorted(intervals, key=lambda i: i[0]):
            if out and i[0] <= out[-1][-1]:
                out[-1].end = max(out[-1].end, i.end)
            else:
                out.append(i)
        return out


nums = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(Solution().merge(nums))
