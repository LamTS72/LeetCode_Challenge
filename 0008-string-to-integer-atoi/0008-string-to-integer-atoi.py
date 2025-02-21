class Solution:
    def myAtoi(self, s: str) -> int:
        if len(s) == 0:
            return 0
        tmp = ""
        sign = "+"
        prev = None
        for st in s:
            if st == " " or st == "+":
                if tmp != "":
                    break
                if prev == "-" or prev == "+":
                    return 0
                if st == " " and (prev == "+" or prev == "-"):
                    return 0
                prev = st
                continue
            
            if st == "-" and tmp == "":
                if prev == "+" or prev == "-":
                    return 0
                prev = st
                sign = st
            elif st.isdigit():
                tmp += st
            else:
                break

        if tmp == "":
            return 0
        else:
            num = int(tmp) if sign == "+" else -int(tmp)
            if num < 0 and num < -2**31:
                num = -2**31
            elif num > 0 and num > 2**31 - 1:
                num = 2**31 - 1
        return num