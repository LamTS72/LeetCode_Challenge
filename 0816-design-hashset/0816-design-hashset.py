class MyHashSet(object):

    def __init__(self):
        self.HashTable = []

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """ 
        if self.contains(key) == False:
            self.HashTable.append(key)
        

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        if key not in self.HashTable:
            return None
        self.HashTable.remove(key)
        

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        if key in self.HashTable:
            return True
        else: 
            return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)