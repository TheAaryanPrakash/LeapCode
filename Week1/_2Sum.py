nums=[2,7,11,15]
target=9
arr=[]
length=len(nums)
for i in range(length):
    for j in range(length):
        if j!=i:
            if (nums[i]+nums[j]==target):
                arr.append(i)
                arr.append(j)
                print(arr)
