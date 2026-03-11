prod = input("digite: ").upper()
i = 0
t = 0

while i < len(prod):
	
	if prod[i] == 'B':
		t = t + 3.75
	if prod[i] == 'C':
		t = t + 7.90
	if prod[i] == 'E':
		t = t + 9.85
	i = i + 1
	
print(round(t,2))
	