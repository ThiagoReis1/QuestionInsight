fruta = 5.40
cereal = 8.95
lata = 4.50

com = input("compras:").upper()

acu = 0
i = 0

while i < len(com):
	if com[i] == 'H':
		acu = acu + 5.40
	elif com[i] == 'C':
		acu = acu + 8.95
	elif com[i] == 'L':
		acu = acu + 4.50
	
	i = i + 1
print(round(acu,2))