# 23/June/2025

# https://leetcode.com/problems/decode-the-message/description/

# def decodeMessage(key, message):
#     Output=""
#     charIndex=97
#     dict={}
#     for i in key:
#         if i not in dict and i!=" ":
#             dict[i]=charIndex
#             charIndex+=1
#     print(dict)
#     for i in message:
#         if i==" ":
#             Output+=" "
#         else:
#             Output+=(chr(dict[i]))
#     return Output
    
# print(decodeMessage("eljuxhpwnyrdgtqkviszcfmabo","zwx hnfx lqantp mnoeius ycgk vcnjrdb"))


# https://leetcode.com/problems/jewels-and-stones/submissions/1673140728/

# class Solution:
#     def numJewelsInStones(self, jewels: str, stones: str) -> int:
#         count=0
#         dict={}
#         for i in range(len(jewels)):
                # dict[jewels[i]]=1
#         for i in stones:
#             if i in dict:
                # count+=1
        
#         return count


# https://leetcode.com/problems/isomorphic-strings/submissions/1673908822/

# def isIsomorphic(s,t) -> bool:
#     d1={}
#     d2={}
#     for i in range(len(s)):
#         if(s[i] not in d1 and t[i] not in d2):
#             d1[s[i]]=t[i]
#             d2[t[i]]=s[i]
#         # elif(s[i] in d1 and t[i] in d2):
#         #     if(d1[s[i]]!=t[i] or d2[t[i]]!=s[i]):
#         #         return False
#         # elif((s[i] not in d1 and t[i] in d2) or(s[i] in d1 and t[i] not in d2)):
#         #     return False
#         elif(s[i] in d1 and d1[s[i]]!=t[i]) or (t[i] in d2 and d2[t[i]]!=s[i]):
#             return False
#         # elif(t[i] in d2 and d2[t[i]]!=s[i]):
#         #     return False
        
            
#     return True
    
# print(isIsomorphic("aaabca","kkkmnm"))
        
            
                
# # set usage--to store unordered elements or unique elemts
# set1=set()
# set1={1,2,3,5,22,3,2}
# print(set1)
# set1={1,2,3,4,55,5,2,2,2,2,2,2}
# print(set1)
# set1.add(9)
# print(set1)
# set1.remove(5)
# print(set1)
# # set1.remove(10) (throws error as 10 is not present)

# set1.discard(10) #(discards when if presents or doesn't throw an error)
# print(set1)

# set2={1,2,4,6,9,0,22,44}
# print(set2)
# print(set1.union(set2))
# print(set1.intersection(set2))
# print(set1.difference(set2))
# print(set2.difference(set1))
# print(set1.symmetric_difference(set2))
            
            
# https://leetcode.com/problems/set-mismatch/submissions/1673970606/

# class Solution:
#     def findErrorNums(self, nums: List[int]) -> List[int]:
#         arr=[]
#         s=set()
#         for i in range(len(nums)):
#             if nums[i] in s:
#                 arr.append(nums[i])
#             else:
#                 s.add(nums[i])
#         for i in range(1,len(nums)+1):
#             if i not in s:
#                 arr.append(i)

#         return arr
