class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 1 or s == " ":
            return True
        
        res = ""
        for i in range(len(s)):
            if "a" <= s[i].lower() <= "z" or "0" <= s[i] <= "9":
                res += s[i].lower()
        print(res)
        return res == res[::-1]
