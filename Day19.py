https://leetcode.com/problems/climbing-stairs/description/

https://leetcode.com/problems/add-binary/description/

https://leetcode.com/problems/binary-tree-preorder-traversal/

https://leetcode.com/problems/binary-tree-postorder-traversal/description/

https://leetcode.com/problems/excel-sheet-column-title/description/

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        s=""
        k=1
        while(columnNumber>0):
            s=chr((columnNumber-1)%26+(65))+s
            columnNumber=(columnNumber-1)//26
            
        return s
        

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        arr=[]
        def post(node):
            if node:
                post(node.left)
                post(node.right)
                arr.append(node.val)
        post(root)
        return arr
        

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr=[]
       
        def pre(node):
            if node:
                arr.append(node.val)
                pre(node.left)
                pre(node.right)
            
        pre(root)
        return arr


        

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a,2)+int(b,2))[2:]
        
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i=len(a)-1
        j=len(b)-1
        carry=0
        arr=[]
        while i>=0 or j>=0 or carry:
            digit_a=int(a[i]) if i>=0 else 0
            digit_b=int(b[j]) if j>=0 else 0
            total=digit_a+digit_b+carry
            arr.append(str(total%2))
            carry=total//2
            i-=1
            j-=1
        return "".join(reversed(arr))
        

class Solution:
    def climbStairs(self, n: int) -> int:
        memo={}
        def fib(t):
            if t in memo:
                return memo[t]
            if t==1 or t==2:
                memo[t]=t
                return t
            else:
                k=fib(t-1)+fib(t-2)
                memo[t]=k
                return k
        return fib(n)
            

        