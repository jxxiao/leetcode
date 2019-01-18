class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates.sort()
        self.dfs(candidates, target, 0, [], res)
        return res

    def dfs(self, candidates, target, index, path, res):
        if target < 0:
            return
        if target == 0:
            res.append(path)
            return
        for i in range(index, len(candidates)):
            if i > index and candidates[i] == candidates[i - 1]:
                continue
            self.dfs(candidates, target - candidates[i], i + 1,
                     path + [candidates[i]], res)


candidates = [2, 5, 2, 1, 2]
target = 5
Solution().combinationSum2(candidates, target)