n = input('').upper()
i = 0
total = 0
p = 0
l = 0
m = 0
while i < len(n):
	if n[i] == "C":
		total += 10.50
		p +=1
	if n[i] == "E":
		total += 8.75
		l+=1
	if n[i] == "P":
		total += 17.90
		m+=1
	i+= 1
print(round(total,2), p, l, m)