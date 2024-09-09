class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        letters = "qwertyuiopasdfghjklzxcvbnm0987654321"
        s = s.lower()
        tmp = ""
        for i in range(0, len(s)):
            if s[i] in letters:
                tmp += s[i]
        n = len(tmp)
        print(tmp)
        if n == 1:
            return True
        for i in range(0, n):
            if tmp[i] != tmp[n - 1 - i]:
                return False
        return True
