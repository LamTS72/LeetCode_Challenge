class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        res = ""
        indx = word.find(ch)
        print(indx)
        if indx == -1:
            return word
        temp2 = word[indx+1:]
        temp1 = word[indx::-1]
        res = temp1 + temp2  

        return res
        