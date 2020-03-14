'''
@Description
@Author: jxxiao
@Github: https://github.com/jxxiao
@Date: 2020-03-05 22:58:36
@LastEditors: jxxiao
@LastEditTime: 2020-03-06 17:05:29
'''
#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#
# https://leetcode.com/problems/word-ladder/description/
#
# algorithms
# Medium (27.49%)
# Likes:    2466
# Dislikes: 1005
# Total Accepted:    365K
# Total Submissions: 1.3M
# Testcase Example:  '"hit"\n"cog"\n["hot","dot","dog","lot","log","cog"]'
#
# Given two words (beginWord and endWord), and a dictionary's word list, find
# the length of shortest transformation sequence from beginWord to endWord,
# such that:
#
#
# Only one letter can be changed at a time.
# Each transformed word must exist in the word list. Note that beginWord is not
# a transformed word.
#
#
# Note:
#
#
# Return 0 if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume beginWord and endWord are non-empty and are not the same.
#
#
# Example 1:
#
#
# Input:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]
#
# Output: 5
#
# Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" ->
# "dog" -> "cog",
# return its length 5.
#
#
# Example 2:
#
#
# Input:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
#
# Output: 0
#
# Explanation: The endWord "cog" is not in wordList, therefore no possible
# transformation.
#
#
#
#
#
#

# @lc code=start

import  collections
import string

class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        wordSet = set(wordList)
        queue = collections.deque([(beginWord, 1)])
        ls = string.ascii_lowercase
        visited = set()
        while queue:
            word, dist = queue.popleft()
            if word == endWord:
                return dist
            for i in range(len(word)):
                for j in ls:
                    newWord = word[:i]+j+word[i+1:]
                    if newWord not in visited and newWord in wordSet:
                        queue.append((newWord, dist+1))
                        visited.add(newWord)
        return 0

    def ladderLength2(self, beginWord, endWord, wordList):
        wordSet = set(wordList)

        def nextWords(word, visited):
            for i in range(len(word)):
                for c in string.ascii_lowercase:
                    nextWord = word[:i] + c + word[i+1:]
                    if nextWord in wordSet and nextWord not in visited:
                        yield nextWord

        queue = collections.deque([(beginWord, 1)])
        visited = set()

        while queue:
            word, dist = queue.popleft()
            if word == endWord:
                return dist
            for nextWord in nextWords(word, visited):
                queue.append((nextWord, dist + 1))
                visited.add(nextWord)
        return 0


    def ladderLength3(self, beginWord, endWord, wordList):
        if endWord not in wordList:
            return 0

        wordSet = set(wordList)

        def nextWords(word, visited):
            for i in range(len(word)):
                for c in string.ascii_lowercase:
                    nextWord = word[:i] + c + word[i+1:]
                    if nextWord in wordSet and nextWord not in visited:
                        yield nextWord

        beginQueue = collections.deque([(beginWord)])
        endQueue = collections.deque([(endWord)])

        beginVisited, endVisited = set([beginWord]), set([endWord])
        step = 1
        while beginQueue and endQueue:
            newQueue = beginQueue
            beginQueue = collections.deque()
            while newQueue:
                word = newQueue.popleft()
                for nextWord in nextWords(word, beginVisited):
                    if nextWord in endQueue:
                        return step + 1
                    beginQueue.append(nextWord)
                    beginVisited.add(nextWord)
            step += 1
            beginQueue, endQueue = endQueue, beginQueue
            beginVisited, endVisited = endVisited, beginVisited
        return 0

    def ladderLength4(self, beginWord, endWord, wordList):
        if endWord not in wordList:
            return 0
        wordSet = set(wordList)

        def nextWords(word, visited):
            for i in range(len(word)):
                for c in string.ascii_lowercase:
                    nextWord = word[:i] + c + word[i+1:]
                    if nextWord in wordSet and nextWord not in visited:
                        yield nextWord

        beginSet, endSet = set([beginWord]), set([endWord])
        beginVisited, endVisited = set([beginWord]), set([endWord])
        step = 1
        while len(beginSet) > 0 and len(endSet) > 0:
            tempSet = beginSet
            beginSet = set()
            for word in tempSet:
                for nextWord in nextWords(word, beginVisited):
                    if nextWord in endSet:
                        return step + 1
                    beginSet.add(nextWord)
                    beginVisited.add(nextWord)
            step += 1
            beginSet, endSet = endSet, beginSet
            beginVisited, endVisited = endVisited, beginVisited
        return 0


beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log"]

beginWord = "qa"
endWord = "sq"
wordList = ["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ci","ca","br","ti","ba","to","ra","fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or","rn","au","ur","rh","sr","tc","lt","lo","as","fr","nb","yb","if","pb","ge","th","pm","rb","sh","co","ga","li","ha","hz","no","bi","di","hi","qa","pi","os","uh","wm","an","me","mo","na","la","st","er","sc","ne","mn","mi","am","ex","pt","io","be","fm","ta","tb","ni","mr","pa","he","lr","sq","ye"]

print(Solution().ladderLength3(beginWord, endWord, wordList))

# @lc code=end
