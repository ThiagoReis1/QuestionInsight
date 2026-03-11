count = 0
while True:
	num = int(input())
	if num == -1:
		print(count)
		break
	if num >= 100 and num <= 199:
		count += 1
print()