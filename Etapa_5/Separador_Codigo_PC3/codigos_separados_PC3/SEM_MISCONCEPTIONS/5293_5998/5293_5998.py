n = int(input("Numero inteiro diferente de zero: "))
contpar = 0
contn = 0

while (n != 0):
	if n%2==0:
		contpar = contpar + 1
		contn = contn + 1
	else:
		contn = contn + 1
	n = int(input("numero inteiro diferente de zero"))

porc = (100*contpar)/contn
print(contn)
print(round(porc,2))