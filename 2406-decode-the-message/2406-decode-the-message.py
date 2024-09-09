class Solution(object):
    def decodeMessage(self, key, message):
        """
        :type key: str
        :type message: str
        :rtype: str
        """
        letters = "abcdefghijklmnopqrstuvwxyz"
        key = key.replace(" ","")
        words = []
        for word in key:
            if word not in words:
                words.append(word)
        map_word = []
        for i,j in zip(words,letters):
            map_word.append((i,j))
        print(map_word)
        res = ""
        for i in range(len(message)):
            if message[i] == " ":
                res += " "
            else:
                for j in map_word:
                    if message [i] == j[0]:
                        res += j[1]
        return res

        return ""
        