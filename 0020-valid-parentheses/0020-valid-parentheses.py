class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        while True:
            if "()" in s:
                s = s.replace("()", "")
            elif "{}" in s:
                s = s.replace("{}", "")
            elif "[]" in s:
                s = s.replace("[]", "")
            else:
                return len(s) == 0

        