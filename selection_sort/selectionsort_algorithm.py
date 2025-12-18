import random 
nums = []

for i in range(0,100):
     nums.append(random.randint(0,100))

for i in range(0,len(nums)):
        check_element = nums[i]
        index = 0
        for x  in range(i,len(nums)):
            if nums[x] < check_element:
                check_element = nums[x]
                index = x         
                nums[i], nums[index] = nums[index], nums[i]