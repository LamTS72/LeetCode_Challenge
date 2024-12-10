class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Solution: loop
        # Requirement: O(n)
        if len(s) == 0 or s == " " or len(s) == 1:
            return True
        letters = "qwertyuiopasdfghjklzxcvbnm1234567890"
        letters = set(letters)

        res = ""
        for i in range(len(s)):
            if s[i].lower() in letters:
                res += s[i].lower()
        print(res)
        for i in range(len(res)):
            if res[i] != res[len(res) - 1 - i]:
                return False
        return True
