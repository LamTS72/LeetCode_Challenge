class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        while len(command):
            if '()' in command:
                command = command.replace('()', 'o')
            elif '(' in command:
                command = command.replace('(', '')
            elif ')' in command:
                command = command.replace(')', '')
            else:
                return command           