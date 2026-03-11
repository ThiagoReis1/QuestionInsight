from numpy import*
string = input(" "). upper()
q1,q2,q3 = 0,0,0
i = 0
p = 0
r = 0
m = 0

while (i < len(string)):
	if (string[i] == "M"):
		m = m + 7.25
		q1 += 1
	if (string[i] == "P"):
		p = p + 4.75
		q2 += 1
	if (string[i] == "R"):
		r = r + 3.50
		q3 += 1
	i += 1
print (p + m + r)