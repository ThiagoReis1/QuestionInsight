s = input("string: ")
i = 0
total =0
while i<len(s):
	if s[i] == 'I':
		total = total + 3.75
	if s[i] == 'M':
		total = total + 4.50
	if s[i] == 'S':
		total =total + 2.90
	i = i +1	
print(round(total,2))