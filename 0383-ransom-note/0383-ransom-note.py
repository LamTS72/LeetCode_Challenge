class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        vocab = {}
        for i in range(len(magazine)):
            if magazine[i] in vocab:
                vocab[magazine[i]] += 1
            else:
                vocab[magazine[i]] = 1

        for s in ransomNote:
            if s not in vocab:
                return False
            else:
                if vocab[s] < 1:
                    return False
                else:
                    vocab[s] -= 1
        return True