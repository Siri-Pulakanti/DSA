# def stairCasePattern(m):
#     for i in range(m):
#         for j in range(i+1):
#             print("*",end="")
#         print()

# stairCasePattern(4) 

# def pyramid(m):
#     for i in range(m):
#         for j in range(m-i-1):
#             print(" ",end="")
#         for j in range(2*i+1):
#             if(j%2==1):
#                 print(" ",end="")
#             else:
#                 print("*",end="")
#         print()
        
# pyramid(8)
        
# def revPyramid(m):
#     for i in range(m,0,-1):
#         for j in range(m-i):
#             print(" ",end="")
#         for j in range(2*i+1):
#             if(j%2==1):
#                 print("*",end="")
#             else:
#                 print(" ",end="")
#         print()
        
# revPyramid(8)

# def pyramid(n):
#     for i in range(n-1):
#         for j in range(n-1-i):
#             print(" ",end="")
#         for j in range(2*i+1):
#             if(j%2==1):
#                 print(" ",end="")
#             else:
#                 print("*",end="")
#         print()
       
# def invPyramid(n):
#     for i in range(n):
#         for j in range(i):
#             print(" ",end="")
#         for j in range(2*(n-i)):
#             if(j%2==1):
#                 print(" ",end="")
#             else:
#                 print("*",end="")
#         print()

      
# def rhombus(n):
#     pyramid(n)
#     invPyramid(n)

# rhombus(4)
        
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/solutions/6723515/step-by-step-visualization-beginner-freindly-java-c-python/

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         profit=0
#         leastPrice=prices[0]
#         for i in range(len(prices)):
#             leastPrice=min(prices[i],leastPrice)
#             profit=max(profit,prices[i]-leastPrice)
            
            
#         return profit    

# https://leetcode.com/problems/maximum-difference-between-increasing-elements/description/

# class Solution:
#     def maximumDifference(self, nums: List[int]) -> int:
#         output=-1
#         lowestNumber=nums[0]
#         for i in range(len(nums)):
#             lowestNumber=min(lowestNumber,nums[i])
#             if(nums[i]!=lowestNumber):
#                 output=max(output,nums[i]-lowestNumber)
#         return output
            

        