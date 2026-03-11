p = input('produtos: ').upper()
i = 0
t = 0
D = 0
S = 0
I = 0

while (i < len(p)):
	if (p[i] == 'D'):
		t = t + 2.25
		D = D + 1
	elif (p[i] == 'S'):
		t = t + 4
		S = S + 1
	elif (p[i] == 'I'):
		t = t + 6.9
		I = I + 1
	i = i + 1
		
print(round(t, 2), D, S, I)

