prod = input().upper()
ia = 0
il = 0
ip = 0
total = 0

for x in prod:
	if x == 'A':
			ia += 1
			total += 16.75
	elif x == 'L':
		il += 1
		total += 4.60
	elif x == 'P':
		ip += 1
		total += 2.85
		
print(round(total, 2), ia, il, ip)