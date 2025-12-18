import random 
import time 
import matplotlib.pyplot as plt


nums = []

for y in range(0,100000):
    nums.append(random.randint(1,y+1)) 
    start = time.time()
    for i in range(0,len(nums)):
        check_element = nums[i]
        index = 0
        for x  in range(i,len(nums)):
            if nums[x] < check_element:
                check_element = nums[x]
                index = x         
                nums[i], nums[index] = nums[index], nums[i] # check element gets changed with first unsorted element
    end = time.time()
    dur = end - start
    plt.plot(dur,y+1)

plt.show()
    

