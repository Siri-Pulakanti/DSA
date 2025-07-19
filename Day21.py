https://leetcode.com/problems/first-missing-positive/description/

https://leetcode.com/problems/longest-consecutive-sequence/

https://www.geeksforgeeks.org/problems/minimum-platforms-1587115620/1

https://leetcode.com/problems/minimum-number-of-frogs-croaking/description/

https://leetcode.com/problems/reverse-words-in-a-string/description/

https://leetcode.com/problems/remove-duplicate-letters/description/

https://leetcode.com/problems/binary-tree-level-order-traversal/description/

https://leetcode.com/problems/binary-tree-level-order-traversal-ii/description/

https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

https://leetcode.com/problems/invert-binary-tree/description/

https://leetcode.com/problems/binary-tree-right-side-view/description/

https://leetcode.com/problems/check-balanced-string/description/

https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result=[]
        queue=deque([root])
        count=0
        while queue:
            list=[]
            size=len(queue)
            for i in range(size):
                node=queue.popleft()
                list.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            count+=1
            if count%2==0:
                list.reverse()
            result.append(list)
        return result




        

class Solution:
    def isBalanced(self, num: str) -> bool:
        even_count=0
        odd_count=0
        arr=[]
        for i in range(len(num)):
            arr.append(int(num[i]))
        for i in range(len(arr)):
            if i%2==0:
                even_count+=arr[i]
            else:
                odd_count+=arr[i]
        if(even_count==odd_count):
            return True
        else:
            return False

        

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result=[]
        queue=deque([root])
        while queue:
            list=[]
            size=len(queue)
            for i in range(size):
                node=queue.popleft()
                list.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(list[-1])
        return result



        

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        self.invertTree(root.left)
        self.invertTree(root.right)
        root.left,root.right=root.right,root.left
        return root

        

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        return 1+max(self.maxDepth(root.left),self.maxDepth(root.right))
        
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result=[]
        queue=deque([root])
        while queue:
            level=[]
            size=len(queue)
            for i in range(size):
                node=queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)
        result.reverse()
        return result
                    
        

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result=[]
        queue=deque([root])
        while queue:
            level=[]
            size=len(queue)
            for i in range(size):
                node=queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)
        return result

        
        



        

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        selected=set()
        last_occurance={}
        sta=[]
        for i in range(len(s)):
            last_occurance[s[i]]=i
        for i in range(len(s)):
            if s[i] not in selected:
                while sta and ord(s[i])<ord(sta[-1]) and last_occurance[sta[-1]]>i:
                    selected.remove(sta.pop())
                sta.append(s[i])
                selected.add(s[i])
        return "".join(sta)

        

class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(s.split()))
        

class Solution:
    def reverseWords(self, s: str) -> str:
        arr=[]
        k=""
        for char in s:
            
            if char==" ":
                if k:
                    arr.append(k)
                    k=""
            else:
                k+=char
        if k:
            arr.append(k)
        arr.reverse()
        return " ".join(arr)

            
                



        

class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
       
        c=r=o=a=k=max_frogs=pre_frogs=0
        
        for i in range(len(croakOfFrogs)):
            if croakOfFrogs[i]=='c':
                c+=1
                pre_frogs+=1
            elif croakOfFrogs[i]=='r':
                r+=1
            elif croakOfFrogs[i]=='o':
                o+=1
            elif croakOfFrogs[i]=='a':
                a+=1
            else:
                k+=1
                pre_frogs-=1
            max_frogs=max(max_frogs,pre_frogs)
            
            if not c>=r>=o>=a>=k:
                return -1
        if pre_frogs==0 and c==r and r==o and o==a and a==k:
            return max_frogs
        else:
            return -1







        

#User function Template for python3

class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,arr,dep):
        # code here
        arr.sort()
        dep.sort()
        i=1
        j=0
        count=1
        max_count=1
        n=len(arr)
        while i<n and j<n:
            if arr[i]<=dep[j]:
                i+=1
                count+=1
                max_count=max(count,max_count)
            else:
                count-=1
                j+=1
        return max_count
                

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set()
        count=0
        max_count=0
        for i in range(len(nums)):
            s.add(nums[i])
        if not nums:
            return 0
        for num in s:
            if num-1 not in s:
                count=1
                max_count=max(count,max_count)
                x=num
                while x+1 in s:
                    count+=1
                    x+=1
                    max_count=max(count,max_count)
        return max_count
            


                


        

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        s=set()
        for i in range(len(nums)):
            if nums[i]>=1:
                s.add(nums[i])
        for i in range(1,len(nums)+1):
            if i not in s:
                return i
        return i+1    
    
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n=len(nums)
        for i in range(n):
            while 1<=nums[i]<=n and nums[nums[i]-1]!=nums[i]:
                temp=nums[nums[i]-1]
                nums[nums[i]-1]=nums[i]
                nums[i]=temp
                # nums[i],nums[nums[i]-1]=nums[nums[i]-1],nums[i]
        for i in range(n):
            if nums[i]!=i+1:
                return i+1
        return n+1
        