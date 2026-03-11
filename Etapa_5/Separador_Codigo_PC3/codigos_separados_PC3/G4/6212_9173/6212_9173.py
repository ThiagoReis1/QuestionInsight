num = int(input())
n = 0
while num != -1:
	if num >= 26 and num <= 85:
		n += 1
	num = int(input())
print(n)
