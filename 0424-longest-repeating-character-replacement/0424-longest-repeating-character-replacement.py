class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqs = collections.defaultdict(int)
        res = 0
        i = 0
        
        for j in range(len(s)):
            freqs[s[j]] += 1
            max_freq = max(freqs.values())
            curr_length = j - i + 1
            if curr_length - max_freq > k:
                freqs[s[i]] -= 1
                i += 1
            res = max(res, j - i + 1)
        return res



    