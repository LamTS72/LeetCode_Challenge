class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        n = len(s)
        q = len(p)
        p = sorted(p)
        tmp = ""
        for i in range(n):
            if s[i] in p:
                tmp += s[i]
                if len(tmp) == len(p):
                    if sorted(tmp) == p:
                        res.append(i-(q - 1))
                    tmp = tmp[1:]
            else:
                tmp = ""
        print(res)
        return res

