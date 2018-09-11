# Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation
# sequence(s) from beginWord to endWord, such that:

# Only one letter can be changed at a time
# Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
# Note:

# Return an empty list if there is no such transformation sequence.
# All words have the same length.

# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.

# You may assume beginWord and endWord are non-empty and are not the same.

# Example 1:

# Input:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]

# Output:
# [
#   ["hit","hot","dot","dog","cog"],
#   ["hit","hot","lot","log","cog"]
# ]
# Example 2:

# Input:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]

# Output: []

# Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.

class Solution(object):
    def adjWord(self, word1, word2):
        count = 0
        for ch in range(len(word1)):
            if word1[ch] != word2[ch]:
                count += 1
                
        return True if count == 1 else False
    
    def findPath(self, curr, endWord, curPath, wordList, step):
        if curr == endWord:
            self.solution.append(curPath[:])
            return
        
        for word in wordList:
            temp = word
            if word not in curPath and self.adjWord(curr, word):
                curPath.append(word)
                self.findPath(word, endWord, curPath, wordList, step+1)
                curPath.pop()
                
    def bfs_paths(self, beginWord, endWord, wordList):
        queue = [(beginWord, [beginWord])]
        while queue:
            (vertex, path) = queue.pop(0)
            for _next in wordList:
                if _next not in path and self.adjWord(_next, vertex):
                    if _next == endWord:
                        yield path + [_next]
                    else:
                        queue.append((_next, path + [_next]))
    
    def findLaddersNOTFeasible(self, beginWord, endWord, wordList):
        self.solution = []
        solutions = list(self.bfs_paths(beginWord, endWord, wordList))
        solutions.sort(key=len)
        if len(solutions) > 0:
            baseline = len(solutions[0])
        ans = []
        for _lis in solutions:
            if len(_lis) == baseline:
                ans.append(_lis)
                
        return ans

    def findLadders(self, start, end, dict):
        def buildpath(path, word):
            if word not in prevMap.keys() or len(prevMap[word])==0:
                path.append(word); currPath=path[:]
                currPath.reverse(); result.append(currPath)
                path.pop();
                return
            path.append(word)
            for iter in prevMap[word]:
                buildpath(path, iter)
            path.pop()
        
        result=[]
        prevMap={}
        length=len(start)
        for i in dict:
            prevMap[i]=[]
        candidates=[set(),set()]; current=0; previous=1
        candidates[current].add(start)
        while True:
            current, previous=previous, current
            for i in candidates[previous]:
                if i in dict:
                    dict.remove(i)
            candidates[current].clear()
            for word in candidates[previous]:
                for i in range(length):
                    part1=word[:i]; part2=word[i+1:]
                    for j in 'abcdefghijklmnopqrstuvwxyz':
                        if word[i]!=j:
                            nextword=part1+j+part2
                            if nextword in dict:
                                prevMap[nextword].append(word)
                                candidates[current].add(nextword)
            if len(candidates[current])==0: return result
            if end in candidates[current]: break
        buildpath([], end)
        return result

solution = Solution()
normal_list = ["hot","dot","dog","lot","log","cog"]
no_solution_list = ["hot","dot","dog","lot","log"]
long_list = ["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ci","ca","br","ti","ba","to","ra","fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or","rn","au","ur","rh","sr","tc","lt","lo","as","fr","nb","yb","if","pb","ge","th","pm","rb","sh","co","ga","li","ha","hz","no","bi","di","hi","qa","pi","os","uh","wm","an","me","mo","na","la","st","er","sc","ne","mn","mi","am","ex","pt","io","be","fm","ta","tb","ni","mr","pa","he","lr","sq","ye"]

assert solution.findLaddersNOTFeasible("hit", "cog", normal_list) == [["hit","hot","lot","log","cog"], ["hit","hot","dot","dog","cog"]] or solution.findLaddersNOTFeasible("hit", "cog", normal_list) == [["hit","hot","dot","dog","cog"], ["hit","hot","lot","log","cog"]]
assert solution.findLaddersNOTFeasible("hit", "cog", no_solution_list) == []
# assert solution.findLadders("qa", "sq", long_list) == [[["qa","pa","pt","st","sq"],["qa","la","lt","st","sq"],["qa","ma","mt","st","sq"],["qa","ca","cr","sr","sq"],["qa","la","lr","sr","sq"],["qa","fa","fr","sr","sq"],["qa","ba","br","sr","sq"],["qa","ma","mr","sr","sq"],["qa","ca","ci","si","sq"],["qa","na","ni","si","sq"],["qa","la","li","si","sq"],["qa","ta","ti","si","sq"],["qa","pa","pi","si","sq"],["qa","ba","bi","si","sq"],["qa","ha","hi","si","sq"],["qa","ma","mi","si","sq"],["qa","pa","ph","sh","sq"],["qa","ra","rh","sh","sq"],["qa","ta","th","sh","sq"],["qa","ca","co","so","sq"],["qa","ga","go","so","sq"],["qa","ta","to","so","sq"],["qa","na","no","so","sq"],["qa","la","lo","so","sq"],["qa","pa","po","so","sq"],["qa","ya","yo","so","sq"],["qa","ma","mo","so","sq"],["qa","ha","ho","so","sq"],["qa","la","ln","sn","sq"],["qa","ra","rn","sn","sq"],["qa","ma","mn","sn","sq"],["qa","ca","cm","sm","sq"],["qa","ta","tm","sm","sq"],["qa","pa","pm","sm","sq"],["qa","fa","fm","sm","sq"],["qa","ta","tc","sc","sq"],["qa","na","nb","sb","sq"],["qa","pa","pb","sb","sq"],["qa","ra","rb","sb","sq"],["qa","ya","yb","sb","sq"],["qa","ma","mb","sb","sq"],["qa","ta","tb","sb","sq"],["qa","ga","ge","se","sq"],["qa","la","le","se","sq"],["qa","na","ne","se","sq"],["qa","ra","re","se","sq"],["qa","ba","be","se","sq"],["qa","ya","ye","se","sq"],["qa","fa","fe","se","sq"],["qa","ha","he","se","sq"],["qa","ma","me","se","sq"]]]
print(solution.findLadders("qa", "sq", long_list))