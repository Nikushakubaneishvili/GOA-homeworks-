#classwork N1
nums = [1,2,3,4,5,6,7,8,9,10]
print(nums [0:4])
print(nums [7:9])
print(nums [0:9:2])
print(nums [0:4])
print(nums [5:9])
print(nums [5::-1])

name = ("nikusha")
print(name [1:4])
print(name [::-1])  

#classwork N2
nums.clear()
print(nums) 

nums_cope = nums
print(nums)
print(nums_cope)

nums_copy = nums
nums_copy[0] = "nikusha"
print(nums)
print(nums_copy)
nums = [1,2,3,4,5,6,7,8,9,10]
nums1 = [11,12,13,14,15,16,17,18,19,20]
nums.extend(nums1)
print(nums) 

#classwork N3
names1 = ["robo", "nika", "goga","roma","nika"]
names1.insert(0, "gela")
print(names1)

names2 = ["maiko","gvanca","nene"]
names1.extend(names2)
print(names1) 
