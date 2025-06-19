# https://leetcode.com/problems/score-of-a-string/submissions/1668929248/


# # ///print name n time
# def printName(n,name):
#     for i in range(n):
#         print("Hi", name)
# printName(2,"Reddy")
    
# print mathTable

# def mathTable(n):
#     for i in range(1,11):
#         print(n,"*",i,"=",n*i)
        
# mathTable(4)

# def scoreOfString(s):
#     score=0   
#     for i in range(len(s)-1):
#         score=score+abs(ord(s[i+1])-ord(s[i]))
#     return score
        
# print(scoreOfString("hello"))
        
        
# https://leetcode.com/problems/final-value-of-variable-after-performing-operations/submissions/1668946985/




# def finalValueAfterOperations(arr):
#     score=0
#     for i in range(len(arr)):
    
#         if(arr[i]=="X++" or arr[i]=="++X"):
#             score=score+1
#         else:
#             score=score-1
            
#     return(score)
            
# print(finalValueAfterOperations(["X++","++X","--X","X--"]))

# https://leetcode.com/problems/defanging-an-ip-address/submissions/1669038951/

# def defangIPaddr(address: str) -> str:
#     defangIP=""
#     for i in range(len(address)):
#         if(address[i]=="."):
#             defangIP=defangIP+"[.]"
#         else:
#             defangIP=defangIP+address[i]
#     return defangIP
    

# print(defangIPaddr("255.100.50.0") )   

# def defangIPaddr(address: str) -> str:
#     # address=address.split(".")
#     # address="[.]".join(address)
#     # return address
#     return "[.]".join(address.split("."))
    
# print(defangIPaddr("255.100.50.0"))    
    

# https://leetcode.com/problems/jewels-and-stones/submissions/1669062277/

# def numJewelsInStones(jewels: str, stones: str) -> int:
#     count=0
#     for i in range(len(jewels)):
#         for j in range(len(stones)):
#             if(jewels[i]==stones[j]):
#                 count+=1
#     return count
    
    
# print(numJewelsInStones("xe", "aAAbbbb"))

# str="asas"
# print("A" in str)

# def numJewelsInStones(jewels: str, stones: str) -> int:
#     count=0
#     for i in range(len(stones)):
#         if(stones[i] in jewels):
#             count+=1
            
#     return count
    
# print(numJewelsInStones("Aa", "aAAbbbb"))

# def numJewelsInStones(jewels: str, stones: str) -> int:
#     count=0
#     for stone in stones:
#         if(stone in jewels):
#             count+=1
            
#     return count
    
# print(numJewelsInStones("Aa", "aAAbbbb"))

# https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/submissions/1669383814/

# arr=[2,4,1,3,55,33]
# minElement=arr[0]
# for i in range(1,len(arr)-1):
#     if(minElement>arr[i+1]):
#         minElement=arr[i+1]
# print(minElement)


# def mostWordsFound(sentences) -> int:
#         maxCount=0
#         for sentence in sentences:
#             maxCount=max(maxCount,len(sentence.split()))
#             # if(len(sentence.split()) > maxCount):
#             #     maxCount=len(sentence.split())
#         return maxCount
# print(mostWordsFound(["please wait", "continue to fight", "continue to win"]))

   
# Matrix 2D:
# matrix=[[1,2,3,4],[1,2,3],[4,6,8],[143,143]]
# print(matrix)

# for arr in matrix:
#     print(arr)
    
# for arr in matrix:
#     for i in arr:
#         print(i)

# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         print(matrix[i][j])


# def boxPattern(m,n):
#     for i in range(m):
#         for j in range(n):
#             print('*',end=" ")
#         print()
            
# boxPattern(4,3)
# print("reddy",end=" ")
# print("reeeddddy")


# def starDashPattern(m,n):
#     for i in range(m):
#         for j in range(n):
#             if(j%2==0):
#                 print("*",end=" ")
#             else:
#                 print("_",end=" ")
#         print()
  
# starDashPattern(3,6) 






            

