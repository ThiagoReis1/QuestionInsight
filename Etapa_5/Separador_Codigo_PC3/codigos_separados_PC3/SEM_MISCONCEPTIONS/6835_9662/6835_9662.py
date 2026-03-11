s = input(" ")
total = 0
i = 0
while i < len(s):
	if s[i]=="B":
		total = total + 3.75
	if s[i]=="C":
		total = total + 7.90
	if s[i]=="E":
		total = total + 9.85
	i = i+1
print(round(total, 2))