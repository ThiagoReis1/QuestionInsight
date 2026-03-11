# faça seu código aqui!
tempo = float(input("tempo de permanencia: "))

taxa = 5     #taxa fixa

if tempo < 2:
	valor = taxa + 1.25
elif tempo == 2:
	valor = taxa + 2.25
else:
	valor = taxa + 3.25
print(round(valor, 2))