class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        letters = list("abcdefghijklmnopqrstuvwxyz")
        print(letters)
        keys = []
        key = key.replace(" ", "")
        for s in key:
            if s not in keys:
                keys.append(s)
        print(keys)
        map_table = {}
        for key, letter in zip(keys, letters):
            map_table[key] = letter
        print(map_table)
        res = ""
        for s in message:
            if s == " ":
                res += s
            else:
                res += map_table[s]
        return res