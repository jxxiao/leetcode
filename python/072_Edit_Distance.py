class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len_word1, len_word2 = len(word1), len(word2)
        list_word1, list_word2 = list(word1), list(word2)
        print(len_word1)
        cost = [[0 for i in range(len_word2+1)] for i in range(len_word1+1)]
        for i in range(len_word2+1):
            print(i)
            cost[0][i] = i
        for i in range(len_word1+1):
            cost[i][0] = i
        for i in range(1, len_word1+1):
            for j in range(1, len_word2+1):
                if (list_word1[i-1] == list_word2[j-1]):
                    cost[i][j] = cost[i-1][j-1]
                else:
                    add = cost[i][j-1] + 1
                    delete = cost[i-1][j] + 1
                    update = cost[i-1][j-1] + 1
                    cost[i][j] = min(min(add, delete), update)
        return cost[len_word1][len_word2]


word1 = "horse"
word2 = "ros"
Solution().minDistance(word1, word2)
