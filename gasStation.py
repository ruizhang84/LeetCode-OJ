class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        size = len(gas)
        forward = 0
        backward = size
        left = 0
        
        # special
        if size == 1:
            if gas[0] < cost[0]:
                return -1
            else:
                return 0

        # iterations
        while forward < backward :
            if left + gas[forward] >= cost[forward]:
                left += gas[forward] - cost[forward]
                forward += 1
            else:
                backward = (backward-1)%size
                left += gas[backward] - cost[backward]
                
                
        if gas[backward%size] < cost[backward%size]:
            return -1
        
        return backward%size
        
        
        
