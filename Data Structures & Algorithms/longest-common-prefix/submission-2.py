class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        for i in range(len(strs[0])):
            for j in range(len(strs) - 1):
                if len(strs[j + 1]) == i:
                    return strs[j][0:i]
                c = strs[j][i]
                d = strs[j + 1][i]
                if c != d:
                    return strs[j][0:i]
        return strs[0]