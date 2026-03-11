s = input()
total = 0
s=s.upper()
for i in range(len(s)):
	if s[i]=='B':
		total+=3.75
	elif s[i]=='C':
		total+=7.9
	elif s[i]=='E':
		total+=9.85
print(round(total,2))