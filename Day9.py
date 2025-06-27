https://leetcode.com/problems/valid-parentheses/submissions/1677779123/

https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/description/

https://leetcode.com/problems/minimize-string-length/description/

https://leetcode.com/problems/baseball-game/submissions/1677803160/

https://leetcode.com/problems/next-greater-element-i/description/

https://leetcode.com/problems/min-stack/submissions/1678205195/

https://leetcode.com/problems/implement-queue-using-stacks/description/

https://leetcode.com/problems/make-the-string-great/description/

arr=[1,3,4,2]
[4, 4, 4, -1]
k=[]
for i in range(len(arr)):
    maxE=arr[i]
    for j in range(i+1,len(arr)):
        maxE=max(maxE,arr[j])
        
    if(maxE==arr[i]):
        k.append(-1)
    else:
        k.append(maxE)
print(k)
maxEle=arr[len(arr)-1]
k=[]
for i in range(len(arr)-1,-1,-1):
    currEle=arr[i]
    if(arr[i]<maxEle):
        arr[i]=maxEle
        k.append(arr[i])
    else:
        maxEle=max(currEle,maxEle)
k.append(-1)
print(k)

for i in range(len(arr)-1):
    for j in range(i+1,len(arr)):
        if(arr[j]>arr[i]):
            arr[i]=arr[j]
            break
        else:
            arr[i]=-1
arr[len(arr)-1]=-1
print(arr)





    