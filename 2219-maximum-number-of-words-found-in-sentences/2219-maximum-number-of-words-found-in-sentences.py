class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        res = 0
        for i in range(len(sentences)):
            if res < len(sentences[i].split(" ")):
                res = len(sentences[i].split(" "))
        return res