class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        string1 = ''.join(word1)
        string2= ''.join(word2)
        return string1 == string2