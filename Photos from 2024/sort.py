def sort(nums):
    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j]>nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp

nums = [1,2,3,4,5,6,7,8,9,10,19,16,17,13,15,]

sort(nums)

print(nums)

""""
def sort(nums):
    for i in range(len(nums)):
        minpos = i
        for j in range(i,len(nums)):
            if nums[j]<nums[minpos]:
                minpos = j
        temp = nums[i]
        nums[i] = nums[minpos]
        nums[minpos] = temp
        print(nums)


nums=list(input("enter n number of values:"))
sort(nums)
print(nums)
"""