class MyHashMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.N = 20011
        self.vec = [[] for _ in range(self.N)]
    
    def find(self, key):
        for pair in self.vec[key % self.N]:
            if pair[0] == key:
                return pair
        return None
        
    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: void
        """
        index = key % self.N
        pair = self.find(key)
        if pair:
            pair[1] = value
        else:
            self.vec[key % self.N].append([key, value])
        

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        index = key % self.N
        pair = self.find(key)
        if pair:
            return pair[1]
        else:
            return -1

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: void
        """
        index = key % self.N
        for i, pair in enumerate(self.vec[index]):
            if pair[0] == key:
                self.vec[index].pop(i)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
