class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = []
        self.maps = {}          # array of index of array

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.maps:
            self.arr.append(val)
            self.maps[val] = len(self.arr)-1
            return True
        
        return False

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.maps:
            return False
        
        #index of val in array
        index = self.maps[val]
        if index != len(self.arr) -1:
            self.maps[self.arr[-1]] = index
            self.arr[index], self.arr[-1] = self.arr[-1], self.arr[index]
        
        #exchange, so to pop
        self.arr.pop()
        
        del self.maps[val]
        return True

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        
        return random.sample(self.arr, 1)[0]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()



