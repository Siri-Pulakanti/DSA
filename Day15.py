https://leetcode.com/problems/sort-colors/

https://leetcode.com/problems/most-frequent-even-element/

https://leetcode.com/problems/majority-element-ii/description/

https://leetcode.com/problems/rearrange-array-elements-by-sign/description/

https://leetcode.com/problems/factorial-trailing-zeroes/description/

https://www.geeksforgeeks.org/problems/equilibrium-point-1587115620/1

https://www.geeksforgeeks.org/problems/missing-number-in-array1416/1

https://leetcode.com/problems/product-of-array-except-self/description/

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        # Output array initialized with 1s
        ans = [1] * n

        # Step 1: Compute prefix products (product of all elements to the left)
        prefix = 1
        for i in range(n):
            ans[i] = prefix
            prefix *= nums[i]

        # Step 2: Multiply with suffix products (product of all elements to the right)
        suffix = 1
        for i in range(n - 1, -1, -1):
            ans[i] *= suffix
            suffix *= nums[i]

        return ans

        
        

class Solution:
    def missingNum(self, arr):
        sum=0
        for i in range(1,len(arr)+2):
            sum=sum^i
        
        for i in range(len(arr)):
            sum=sum^arr[i]
        return sum
            
        
       
        # code here

# User function Template for python3

class Solution:
    #Function to find equilibrium point in the array.
    def findEquilibrium(self, arr):
        # code here
        ts=sum(arr)
        ls=0
        rs=0
        for i in range(1,len(arr)-1):
            ls=ls+arr[i-1]
            rs=ts-ls-arr[i]
            if(ls==rs):
                return i
        return -1



class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pos=[]
        neg=[]
        for num in nums:
            if num<0:
                neg.append(num)
            else:
                pos.append(num)
        k=[]
        i=0
        for i in range(len(nums)//2):
            k.append(pos[i])
            k.append(neg[i])
            
        return k
        

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        LE1=0
        c1=0
        LE2=0
        c2=0
        for i in range(len(nums)):
            if c1==0 and nums[i]!=LE2:
                c1=1
                LE1=nums[i]
            elif c2==0 and nums[i]!=LE1:
                c2=1
                LE2=nums[i]
            elif nums[i]==LE1:
                c1+=1
            elif nums[i]==LE2:
                c2+=1
            else:
                c1-=1
                c2-=1
        target=len(nums)//3
        c1=0
        c2=0
        for i in range(len(nums)):
            if(nums[i]==LE1):
                c1+=1
            elif nums[i]==LE2:
                c2+=1
        a=[]
        if(c1> target):
            a.append(LE1)
        if(c2> target):
            a.append(LE2)
        return a

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c=1
        LE=nums[0]
        for i in range(1,len(nums)):
            if c==0:
                LE=nums[i]
                c+=1
            elif nums[i]==LE:
                c+=1
            else:
                c-=1
        return LE
        
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        s=0
        m=0
        e=len(nums)-1
        while(m<=e):
            if nums[m]==2:
                nums[m],nums[e]=nums[e],nums[m]
                
                e-=1
            elif nums[m]==0:
                nums[s],nums[m]=nums[m],nums[s]
                s+=1
                m+=1
            else:

                m+=1
        return nums

class Solution(object):
    def mostFrequentEven(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict1={}
        for num in nums:
            if num%2==0:
                if num in dict1:
                    dict1[num]+=1
                else:
                    dict1[num]=1
        
        
        max_count=0
        max_ele=0
        
        for j in dict1:
            if dict1[j]>max_count:
                max_count=dict1[j]
                max_ele=j
            elif dict1[j]==max_count and j<max_ele:
                max_ele=j
        if max_count==0:
            return -1
        else:
            return max_ele
                
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        k=5
        ans=0
        while(n//k>=1):
            ans+=n//k
            k=k*5
        return ans


        
        


        

           

            
