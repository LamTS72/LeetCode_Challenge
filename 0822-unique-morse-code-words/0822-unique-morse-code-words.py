class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        list_map = []
        for i in range(len(morse)):
            tmp = [chr(97+i),morse[i]]
            list_map.append(tmp)
        print(list_map)
        list_morse_str = []
        for i in range(len(words)):
            tmp = ""
            for k in range(len(words[i])):
                for j in range(len(list_map)):
                    if list_map[j][0] == words[i][k]:
                        tmp += list_map[j][1]

            list_morse_str.append(tmp)
        print("list ",list_morse_str)
        res = len(set(list_morse_str))
        return res


        