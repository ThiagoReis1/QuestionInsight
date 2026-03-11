nums = list(eval(input()))

i, pontos = 0, 0
while (i < len(nums)):
	if (nums[i] == 1):
		pontos = pontos + 80
	elif (nums[i] == 2):
		pontos = pontos + 40
	elif (nums[i] == 3):
		pontos = pontos + 20
	elif (nums[i] == 4):
		pontos = pontos + 10
	i = i + 1
	
print(pontos)