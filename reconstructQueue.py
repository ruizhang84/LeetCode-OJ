class Solution:
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(people) <2:
            return people
        
        ans = []
        old = sorted(people, key=lambda a: (-a[0], a[1]))
        for t in old:
            ans.insert(t[1], t)

        return ans
