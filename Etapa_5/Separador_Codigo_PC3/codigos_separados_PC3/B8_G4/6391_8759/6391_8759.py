from numpy import*
nums=array(eval(input()))

for i in range(size(nums)):
	if nums[i] == 0:
		nums[i] = 9 ** 3
	elif nums[i]== 1:
		nums[i] = 0
	elif nums[i] == 2:
		nums[i]= 1 ** 3
	elif nums[i] == 3:
		nums [i] = 2 **3
	elif nums[i] == 4:
		nums[i] = 3 **3
	elif nums[i]== 5:
		nums[i]= 4**3
	elif nums[i]== 6:
		nums[i] = 5 **3
	elif nums[i] == 7:
		nums[i] = 6**3
	elif nums[i] == 8:
		nums[i] = 7 **3
	elif nums[i] == 9:
		nums[i] = 8 **3
print(nums)
	