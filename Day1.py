# print statements
print("Hello Siri!!!")
#varaible declaration
name = "Siri Chandana"
age = 16
print(name)
#conditionals
#indentation
if(age >= 18):
 print("You are eligible to vote")
 print("You are eligible to vote")
else:
    print("You are NOT eligible to vote")


# array declaration
names = ["Siri", "Buddamma", "Bangaram"]
# print(names[0])

#traversing an array
# for name in names:
#     print(name)
    
# Array traversal using range
# for i in range(len(names)):
#     print(i)
#     print(names[i])

# Array traversal in reverse
# for i in range(len(names)):
#     print(len(names)-i-1)
#     print(names[len(names)-i-1])

# Array traversal in reverse
# for i in range(len(names)-1, -1, -1):
#     print(i)
#     print(names[i])

# range starts from 0 to given number(exclusive)
# for i in range(5):
#     print(i+1)
    
    
# starting number & ending number (exclusive)
# for i in range(5, 9):
#     print(i)

#starting number, ending number (exclusive), step
# for i in range(5, 12, 2):
#     print(i)

# for i in range(12, 5, -1):
#     print(i)

arr=[1,2,4,5,7,33,55,2,1,2,1]
count=0
for i in arr:
    if(i==1):
        count=count+1
print(count)

arr=[5,6,2,3,8]
count=0
for i in arr:
    if i%3==0:
        print(i, "is divisible by 3")
        count=count+1
print(count)

arr=[5,6,23,36,46,98,180]
count=0
for i in range(len(arr)):
    if(arr[i]%6==0):
        
     print(arr[i],"is divisible by 6")
     count=count+1
print(count)

