count = 0 
while True:
	num = int(input())
	if num < 0:
		break
	if 76 <= num <= 100:
		count += 1 
print(count)