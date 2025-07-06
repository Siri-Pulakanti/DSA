https://leetcode.com/problems/longest-consecutive-sequence/description/

https://leetcode.com/problems/trapping-rain-water/description/

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        leftMax=[0]
        rightMax=[0]
        count=0
        k=height[0]
        for i in range(0,len(height)):
            k=max(k,height[i])
            leftMax.append(k)
        k=height[-1]
        for i in range(len(height)-2,-1,-1):
            k=max(k,height[i])
            rightMax.append(k)
        rightMax.reverse()
        k=0
        for i in range(len(height)):
            k=min(leftMax[i],rightMax[i])
            if(height[i]<k):
                count+=k-height[i]
        return count


        

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        dict1={}
        existingDt={}
        maxCount=0
        for num in nums:
            if num in dict1:
                dict1[num]+=1
            else:
                dict1[num]=1

        for num in nums:
            if num in existingDt:
                continue
            count=1
            left=num
            right=num
            while left+1 in dict1:
                count+=1
                existingDt[left]=1
                left+=1
            while right-1 in dict1:
                count-=1
                existingDt[right]=1
                right-=1
            maxCount=max(maxCount,count)
        return maxCount


        
        

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        nums.sort()
        count=1
        maxCount=1

        for i in range(1,len(nums)):
            if(nums[i-1]+1==nums[i]):
                count+=1
                maxCount=max(maxCount,count)
            elif(nums[i]==nums[i-1]):
                continue
            else:
                count=1
        return maxCount
        