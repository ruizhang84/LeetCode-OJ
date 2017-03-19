class Solution:
    def largestNumber(self, nums):
        ans = ''
        st = [str(s) for s in nums]
        st.sort(cmp_items)
        if st[0] == '0':
            return '0'
        
        return ''.join(st)
        
        
        
def cmp_items(a, b):
    if a[0] == b[0]:
        c = a + b
        d = b + a
        if c < d:
            return 1
        elif c == d:
            return 0
        else:
            return -1
                
    else:
        if a < b:
            return 1
        elif a == b:
            return 0
        else:
            return -1
        
        
        
