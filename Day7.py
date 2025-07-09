24-June 2025

//subarrays of an array
arr=[1,8,9]
ans=[]
for i in range(len(arr)):
    temp=[]
    for j in range(i,len(arr)):
        temp.append(arr[j])
        ans.append(temp.copy())
print(ans)

        return arr [[1], [1, 8], [1, 8, 9], [8], [8, 9], [9]]

Substring of a string

str="sir"
ans=[]
for i in range(len(str)):
    temp=""
    for j in range(i,len(str)):
        temp+=(str[j])
        ans.append(temp)
print(ans)

['s', 'si', 'sir', 'i', 'ir', 'r']

Find the highest sum of subarray of length 3 in below array. (Worst O(n^3))

li=[5,9,1,8,7,6]
arr=[]
maxii=0
for i in range(len(li)-2):
    sum=0
    for j in range(i,i+3):
        sum+=li[j]
        arr.append(sum)
        
for i in range(len(arr)):
    maxii=max(maxii,arr[i])
print(maxii)



Sliding Window
def slidingWindow(a,sal):
    tempSum=0
    maxSum=0
    lp=0
    for i in range(len(a)):
        tempSum+=a[i]
        if(i-lp==sal):
            tempSum-=a[lp]
            lp+=1
        if(i-lp+1==sal):
            maxSum=max(maxSum,tempSum)
    return maxSum
            
       


print(slidingWindow([5,4,1,8,7],3))

https://www.geeksforgeeks.org/problems/max-sum-subarray-of-size-k5313/1

class Solution:
    def maximumSumSubarray (self,arr,k):
        maxSum=0
        tempSum=0
        lp=0
        for i in range(len(arr)):
            tempSum+=arr[i]
            if(i-lp==k):
                tempSum=tempSum-arr[lp]
                lp=lp+1
            if(i-lp+1==k):
                maxSum=max(maxSum,tempSum)
        return maxSum