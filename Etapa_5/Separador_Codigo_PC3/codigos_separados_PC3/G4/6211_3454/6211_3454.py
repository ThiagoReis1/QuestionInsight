cnt = 0
n = int(input())
while n != -1:
	if n >= 100 and n <= 199:
		cnt += 1
	n = int(input())
print(cnt)