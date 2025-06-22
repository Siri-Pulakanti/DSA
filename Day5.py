# https://leetcode.com/problems/two-furthest-houses-with-different-colors/

# def maxDistance( colors):
#     difference=0
   
#     for i in range(len(colors)):
#         currentColor=colors[i]
#         index=i
#         for j in range(i+1,len(colors)):
#             if(currentColor!=colors[j]):
#                 difference=max(difference,abs(index-j))
#     return difference

# print(maxDistance([0,1]))

# class Solution:
#     def maxDistance(self, colors: List[int]) -> int:
#         difference=0
#         currentColor=colors[0]
#         index=0
#         for i in range(len(colors)):
#             if(currentColor!=colors[i]):
#                 difference=max(difference,abs(index-i))
#         index=len(colors)-1
#         currentColor=colors[len(colors)-1]
#         for i in range(len(colors)-2,0,-1):
#             if(currentColor!=colors[i]):
#                 difference=max(difference,abs(index-i))
#         return difference

# https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/submissions/1672536292/

# class Solution:
#     def replaceElements(self, arr: List[int]) -> List[int]:
#         rightMaxTillNow=arr[len(arr)-1]
#         for i in range(len(arr)-2,-1,-1):
#             temp=arr[i]
#             arr[i]=rightMaxTillNow
#             rightMaxTillNow=max(rightMaxTillNow,temp)
#         arr[len(arr)-1]=-1
#         return arr

# name=input()
# age=int(input())
# print("I am",name,"of age",age)
# print(type(name))
# print(type(age))


# names=[]
# for i in range(2):
#     names.append(input())
    
# print(names)


# li=[]
# s=input()
# k=(s.split())
# for i in range(len(k)):
#     li.append(k[i])
    
#   print(li)
# def convert(val):
#     try:
#         return int(val)
#     except ValueError:
#         return val

# lis=list(map(convert,input().split()))
# print(lis)

# li=[4,5,7,1,3,2]
# print(sorted(li))
# print(li)

# li.sort(reverse=True)
# print(li)


# BUBBLE SORT
# def bubbleSort(arr):
#     for i in range(len(arr)-1,0,-1):
#         for j in range(i):
#             isSwap=False
#             if(arr[j]>arr[j+1]):
#                 arr[j],arr[j+1]=arr[j+1],arr[j]
#                 isSwap=True
#         if(isSwap==False):
#             return(arr)
            
#     return(arr)
    
# print(bubbleSort([3,1,2,5,22,6,7]))


# dict={"name":"siri","age":26}
# print(dict)
# dict["gender"]="F"
# if "marks" in dict:
#     print(dict["marks"])
# else:
#     print("lev")
# for i in dict:
#     print(i,":",dict[i])




# arr=[1,5,8,0,1,8,1,5,1]
# dict={}
# for i in range(len(arr)):
#     if arr[i] in dict:
#         dict[arr[i]]=dict[arr[i]]+1
#     else:
#         dict[arr[i]]=1
       
# print(dict)        
        
# def majorityElement(nums) -> int:
#     dict={}
#     for i in range(len(nums)):
#         if nums[i] in dict:
#             dict[nums[i]]=dict[nums[i]]+1
#         else:
#             dict[nums[i]]=1
   
#     for i in dict:
#         if(dict[i]>len(nums)/2):
#             return(i)   
# print(majorityElement([3,2,3]))


# dict={"name":"Siri"}
# if "age" in dict:
#     dict["age"]+=1
# else:
#     dict["age"]=25
# print(dict)

# for i in dict:
#     print("key :",i,"Value:",dict[i])
    
# if "age" in dict:
#     dict["age"]+=1
# else:
#     dict["age"]=25
# print(dict)

# https://leetcode.com/problems/majority-element/description/


# class Solution:
#         def majorityElement(self, nums: List[int]) -> int:
#             return sorted(nums)[len(nums)//2]
#             dict={}
#             for i in range(len(nums)):
#                 if nums[i] in dict:
#                     dict[nums[i]]=dict[nums[i]]+1
#                 else:
#                     dict[nums[i]]=1
#             for i in dict:
#                 if(dict[i]>len(nums)/2):
#                     return i








