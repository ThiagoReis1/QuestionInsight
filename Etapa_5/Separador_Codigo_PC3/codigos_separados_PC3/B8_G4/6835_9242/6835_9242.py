prod = input('produtos:').upper()
bis = 0
cer = 0
enl = 0
i = 0
while(i < len(prod)):
	if(prod[i] == 'B'):
		bis += 1
	elif(prod[i] == 'C'):
		cer += 1
	elif(prod[i] == 'E'):
		enl += 1
	i += 1
bis1 = (bis * 3.75)
cer1 = (cer * 7.90)
enl1 = (enl * 9.85)
valor = (bis1 + cer1 + enl1)
print(round(valor, 2))