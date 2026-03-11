c = 0

while True:
	n = int(input())
	
	if n < 0:
		break
	
	if 100 <= n <=199:
	 c += 1
	
print(c)