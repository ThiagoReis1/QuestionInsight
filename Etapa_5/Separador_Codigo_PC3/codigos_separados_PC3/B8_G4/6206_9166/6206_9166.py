i = 0
while True:
	n = int(input())
	if (n == -1):
		break
	elif (n >= 0 and n <= 25):
		i = i + 1
		
print(i)