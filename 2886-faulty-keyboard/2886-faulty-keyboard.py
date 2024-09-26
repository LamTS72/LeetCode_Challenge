class Solution:
    def finalString(self, s: str) -> str:
        num_i = s.count("i")
        for _ in range(num_i):
            idx = s.find("i")
            prefix_s = s[:idx]
            s = str(prefix_s[::-1]) + s[idx+1:]
        print(s)
        return s