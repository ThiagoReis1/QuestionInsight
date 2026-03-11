compra= float(input())
cp =input()
if cp == "D" or cp == "P":
	valor= compra * 0.89
elif cp == "C":
	v= int(input())
	if v == 1:
		valor = compra
	elif v == 2:
		valor = compra * 1.06
else:
	print()
print(round(valor, 2))