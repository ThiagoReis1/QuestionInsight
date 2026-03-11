s = input('')

i = 0
total = 0 

while i < len(s):
	if s[i] == 'A':
		total += 19.9
	elif s[i] == 'L':
		total += 3.5
	elif s[i] == 'P':
		total += 4.25
	i += 1
print(round(total,2))