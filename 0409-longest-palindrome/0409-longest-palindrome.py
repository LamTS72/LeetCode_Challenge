class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        vocab = {}
        for i in range(len(s)):
            if s[i] in vocab:
                vocab[s[i]] += 1
            else:
                vocab[s[i]] = 1
        
        length = 0
        flag = False
        for freq in vocab.values():
            if freq % 2 == 0:
                length += freq
            else:
                length += freq - 1
                flag = True
        if flag:
            length += 1
        return length
