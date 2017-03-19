class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        elif len(matrix) == 1:
            return searchrow(matrix, 0, target)
        elif len(matrix[0]) == 1:
            return searchcol(matrix, 0, target)
        
        top0, top1 = 0, 0
        bottom0, bottom1 = len(matrix)-1, len(matrix[0])-1
        if  top0 == bottom0 - 1 and top1 == bottom1 -1:
            return matrix[top0][top1] == target or matrix[top0][bottom1] == target or matrix[bottom0][top1] == target or matrix[bottom0][bottom1] == target
        
        mid0, mid1 = (top0 + bottom0)/2, (top1 + bottom1)/2
        if matrix[mid0][mid1] > target:
            return recur_search(matrix, top0, top1, mid0, mid1, target) or recur_search(matrix, mid0, top1, bottom0, mid1, target) or recur_search(matrix, top0, mid1, mid0, bottom1, target) 
        elif matrix[mid0][mid1] < target:
            return recur_search(matrix, mid0, mid1, bottom0, bottom1, target) or recur_search(matrix, mid0, top1, bottom0, mid1, target) or recur_search(matrix, top0, mid1, mid0, bottom1, target)  
            
        return True

def searchrow(matrix, row, target):
    left, right = 0, len(matrix[0])-1
    while left <= right:
        mid = (left + right)/2
        if matrix[row][mid] > target:
            right = mid-1
        elif matrix[row][mid] < target:
            left = mid+1
        else:
            return True
        
    return False

def searchcol(matrix, col, target):
    left, right = 0, len(matrix)-1
    while left <= right:
        mid = (left + right)/2
        if matrix[mid][col] > target:
            right = mid-1
        elif matrix[mid][col] < target:
            left = mid+1
        else:
            return True
        
    return False
        
def recur_search(matrix, top0, top1, bottom0, bottom1, target):
    if target < matrix[top0][top1] or target > matrix[bottom0 ][ bottom1]:
        return False
        
    if  top0 == bottom0 :
        return searchrow(matrix, top0, target)
    if  top1 == bottom1 :
        return searchcol(matrix, top1, target)
    if  top0 == bottom0 - 1 and top1 == bottom1 -1:
        return matrix[top0][top1] == target or matrix[top0][bottom1] == target or matrix[bottom0][top1] == target or matrix[bottom0][bottom1] == target

    mid0, mid1 = (top0 + bottom0)/2, (top1 + bottom1)/2
    if matrix[mid0][mid1] > target:
        return recur_search(matrix, top0, top1, mid0, mid1, target)  or recur_search(matrix, mid0, top1, bottom0, mid1, target) or recur_search(matrix, top0, mid1, mid0, bottom1, target)  
    elif matrix[mid0][mid1] < target:
        return recur_search(matrix, mid0, mid1, bottom0, bottom1, target) or recur_search(matrix, mid0, top1, bottom0, mid1, target) or recur_search(matrix, top0, mid1, mid0, bottom1, target) 
        
    return True



