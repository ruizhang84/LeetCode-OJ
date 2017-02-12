class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) < 4 or len(s) > 12:
            return []
        ans = []
        
        temp = []
        temp.append(s[:1])
        recur_IP(ans, temp, s[1:], 0)
        temp.pop()
        
        if s[0] != '0':
            temp.append(s[:2])
            recur_IP(ans, temp, s[2:], 0)
            temp.pop()
        else:
            return ans
        
        if int (s[:3]) <= 255:
            temp.append(s[:3])
            recur_IP(ans, temp, s[3:], 0)   
            temp.pop()
        return ans

def recur_IP(ans, base, s, idx):
    if idx == 3:
        return
    
    if len(s) < 1:
        return
    temp = base[:]
    temp.append(s[:1])
    if idx == 2 and len(s) == 1:
        ans.append(".".join(temp))
        return
    else:
        recur_IP(ans, temp, s[1:], idx+1)
    temp.pop()
        
    if len(s) < 2:
        return
    if s[0] != '0':
        temp.append(s[:2])
        if idx == 2 and len(s) == 2:
            ans.append(".".join(temp))
            return
        else:
           recur_IP(ans, temp, s[2:], idx+1)
        temp.pop()
    else:
        return
    
    if len(s) <3:
        return 
    if int (s[:3]) <= 255:
        temp.append(s[:3])
        if idx == 2 and len(s) == 3:
            ans.append(".".join(temp))
            return
        else:
            recur_IP(ans, temp, s[3:], idx+1)   
        temp.pop()

    
        
