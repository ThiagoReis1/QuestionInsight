str = input().upper()
count = 0
while (str != 'X'):
	if (str == 'A'):
		count += 1
	str = input().upper()
print(count)