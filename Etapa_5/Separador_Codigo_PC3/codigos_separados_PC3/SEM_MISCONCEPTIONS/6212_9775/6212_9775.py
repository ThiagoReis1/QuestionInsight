number = int(input())
count = 0

while number != -1:
	if number >= 26 and number <= 85:
		count += 1
	number = int(input())
print(count)