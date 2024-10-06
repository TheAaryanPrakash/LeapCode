nums=[2,0,2,1,1,0]
x=nums.count(0)
y=nums.count(1)
z=nums.count(2)
del nums[:]
for i in range(x):
    nums.append(0)
for i in range(y):
    nums.append(1)
for i in range(z):
    nums.append(2)
print(nums)
