class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        tmp1 = []
        tmp2 = []
        for i in range(len(word1)):
            tmp1 += word1[i] 
        for i in range(len(word2)):
            tmp2 += word2[i] 

        return tmp1 == tmp2