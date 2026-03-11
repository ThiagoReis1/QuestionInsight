num = int(input())

count = 0

while (num != -1):
	if (num >= 26 and num < 85):
		count += 1
	num = int(input())
print(count)