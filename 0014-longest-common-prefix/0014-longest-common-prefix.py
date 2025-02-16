class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        
        for i in range(len(strs[0])):
            s = strs[0][i]
            for word in strs[1:]:
                if i == len(word) or s != word[i]:
                    return strs[0][0:i]
        return strs[0]