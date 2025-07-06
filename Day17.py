https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/

https://leetcode.com/problems/search-in-a-binary-search-tree/description/

https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/

https://leetcode.com/problems/minimum-absolute-difference-in-bst/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        arr=[]
        def inOrder(r):
            if not r:
                return None
            inOrder(r.left)
            arr.append(r.val)
            inOrder(r.right)
        
        inOrder(root)

        
        mini=arr[1]-arr[0]
        for i in range(1,len(arr)):
            mini=min(mini,arr[i]-arr[i-1])
        return mini
        

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        
        if root.val>max(p.val,q.val):
            return self.lowestCommonAncestor(root.left,p,q)
        elif root.val<min(p.val,q.val):
            return self.lowestCommonAncestor(root.right,p,q)
        else:
            return root

        

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        if not root:
            return None
        if root.val>val:
            return self.searchBST(root.left,val)
        elif root.val<val:
            return self.searchBST(root.right,val)
        else:
            return root



        

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        if not nums:
            return None
        
        mid=len(nums)//2
        root=TreeNode(nums[mid])
        root.left=self.sortedArrayToBST(nums[:mid])
        root.right=self.sortedArrayToBST(nums[mid+1:])
        return root


        