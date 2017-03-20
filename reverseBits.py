class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        temp = bin(n)[2:][::-1]
        return int(temp + '0'*(32-len(temp)), 2)

        
        
