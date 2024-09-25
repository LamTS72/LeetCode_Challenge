class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        res = 0
        for sent in sentences:
            s = sent.split(" ")
            res = max(res, len(s))
        return res