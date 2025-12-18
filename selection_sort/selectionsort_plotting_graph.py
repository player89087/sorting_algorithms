import random 
import time 
import matplotlib.pyplot as plt


nums = []
duration = []
size = []
for y in range(0,5000): # change here how many you want to sort
    print(y)
    nums.append(random.randint(1,100)) 
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
    duration.append(dur)
    size.append(y+1)

plt.plot(size,duration)

plt.show()
    

