vtc = float(input())
cop = input()

if cop == "C":
	debito = int(input('1 ou 2 vezes?'))
	if debito == 1:
		preco = vtc 
	elif debito == 2:
		preco = vtc + (vtc * 9/100)
else: 
	preco = vtc - (vtc * 19/100)
print(round(preco, 2))