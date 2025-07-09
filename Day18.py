https://leetcode.com/problems/minimum-distance-between-bst-nodes/description/

https://leetcode.com/problems/minimum-absolute-difference-in-bst/description/

https://leetcode.com/problems/increasing-order-search-tree/description/

https://leetcode.com/problems/increasing-order-search-tree/description/

https://leetcode.com/problems/range-sum-of-bst/description/

https://leetcode.com/problems/insert-into-a-binary-search-tree/description/

https://leetcode.com/problems/first-unique-character-in-a-string/description/

https://leetcode.com/problems/palindrome-number/description/

https://leetcode.com/problems/roman-to-integer/description/

https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/

https://leetcode.com/problems/plus-one/description/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry=1
        
        for i in range(len(digits)-1,-1,-1):
            if carry==0:
                return digits
            else:
                
                sum=digits[i]+carry
                digits[i]=sum%10
                carry=sum//10
        if carry!=0:        
            ans=[1]
            ans.extend(digits)
            return ans
        else:
            return digits

        

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        k=0
        for i in range(len(digits)):
            k=k*10
            k=k+digits[i]
        k=k+1
        arr=[]
        while(k!=0):
            t=k%10
            arr.append(t)
            k=k//10
        arr.reverse()
        return arr   

        

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l=len(needle)
        s=""
        for i in range(len(haystack)):
            s+=haystack[i]
            if(len(s)==l):
                if(s==needle):
                    return i-l+1
                else:
                    s=s[1:]

        return -1



        

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
        
        

class Solution:
    def romanToInt(self, s: str) -> int:
        dict1={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        score=0
        for i in range(len(s)-1):
            if(dict1[s[i]]<dict1[s[i+1]]):
                score-=dict1[s[i]]
            else:
                score+=dict1[s[i]]
        score+=dict1[s[-1]]
        return score

        

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0 or (x%10==0 and x!=0):
            return False
        
        reve=0
        while(reve<x):
            j=x%10
            reve=reve*10+j
            x=x//10
        if(reve==x or x==reve//10):
            return True
        else:
            return False
        
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        s=str(x)
        y=""
        for i in range(len(s)-1,-1,-1):
            y+=s[i]
        for i in range(len(s)):
            if(y[i]!=s[i]):
                return False
        return True
        
        
        
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        s=str(x)
        
        for i in range(len(s)):
            if(s[i]!=s[len(s)-1-i]):
                return False
        return True
        
        
        
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        y=x
        k=0
        while(x!=0):
            j=x%10
            k=k*10+j
            x=x//10
        if(k==y):
            return True
        else:
            return False
        


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict={}
        for i in range(len(s)):
            if s[i] in dict:
                dict[s[i]]+=1
            else:
                dict[s[i]]=1
        for i in range(len(s)):
            if dict[s[i]]==1:
                return i
        return -1
        

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def insert(node,val):
            if node is None:
                return TreeNode(val)
            if val<node.val:
                node.left=insert(node.left,val)
                
                
            else:
                node.right=insert(node.right,val)
            return node

        return insert(root,val)


        

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        curr=root
        while True:
            if curr.val>val:
                if curr.left:
                    curr=curr.left
                else:
                    curr.left=TreeNode(val)
                    
                    break
            else:
                if curr.val<val:
                    if curr.right:
                        curr=curr.right
                    else:
                        curr.right=TreeNode(val)
                        break
                
        return root


        

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if root is None:
            return 0
        if root.val<low:
            return self.rangeSumBST(root.right,low,high)
        elif root.val>high:
            return self.rangeSumBST(root.left,low,high)
        else:
            return root.val+self.rangeSumBST(root.left,low,high)+self.rangeSumBST(root.right,low,high)

    



        

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.count=0

        def inOrder(node):
            if not node:
                return
            if not node.val<low:
                inOrder(node.left)
            if(node.val>=low and node.val<=high):
                self.count+=node.val
            if not node.val>high:
                inOrder(node.right)
        inOrder(root)
        return self.count

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.count=0

        def inOrder(node):
            if not node:
                return
            inOrder(node.left)
            if(node.val>=low and node.val<=high):
                self.count+=node.val
            inOrder(node.right)
        inOrder(root)
        return self.count

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        dummy_node=TreeNode(-1)
        self.current=dummy_node
        def inOrder(node):
            if not node:
                return
            inOrder(node.left)
            self.current.right=TreeNode(node.val)
            self.current=self.current.right
            inOrder(node.right)

        inOrder(root)
        return dummy_node.right

        

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        arr=[]
        def inOrder(node):
            if not node:
                return
            else:
                inOrder(node.left)
                arr.append(node.val)
                inOrder(node.right)
        inOrder(root)

        new_root=TreeNode(arr[0])
        ans=new_root
        for i in range(1,len(arr)):
            new_root.right=TreeNode(arr[i])
            new_root=new_root.right

        return ans
            


    

        

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.prev_val=None
        self.min_difference=float("inf")
        def inOrder(node):
            if not node:
                return
            else:
                inOrder(node.left)
                if self.prev_val is not None:
                    self.min_difference=min(self.min_difference,node.val-self.prev_val)
                
                self.prev_val=node.val

                inOrder(node.right)

        inOrder(root)
        return self.min_difference

        

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.prev_val=None
        self.min_difference=float("inf")
        def inOrder(node):
            if not node:
                return
            else:
                inOrder(node.left)
                if self.prev_val is not None:
                    self.min_difference=min(self.min_difference,node.val-self.prev_val)
                self.prev_val=node.val
                inOrder(node.right)
        inOrder(root)
        return self.min_difference
        

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        arr=[]
        
        def inOrder(node):
            if not node:
                return
            else:
                inOrder(node.left)
                arr.append(node.val)
                inOrder(node.right)
        inOrder(root)
        min1=arr[1]-arr[0]
        for i in range(1,len(arr)-1):
            min1=min(arr[i+1]-arr[i],min1)
        return min1
        

        