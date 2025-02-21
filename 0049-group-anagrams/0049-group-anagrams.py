class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        if len(strs) == 1:
            res.append(["".join(strs[0])])
            return res
            
        hashmap = dict()
        for i in range(len(strs)):
            tmp = "".join(sorted(strs[i]))
            if tmp not in hashmap:
                hashmap[tmp] = []
            
            hashmap[tmp].append(strs[i])
        print(hashmap)
        return list(hashmap.values())