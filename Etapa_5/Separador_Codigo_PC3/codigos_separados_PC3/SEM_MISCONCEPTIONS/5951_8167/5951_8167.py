opcao = input("Digite T para tapioca e S para salgado: ").upper()
quantopcao = int(input("Digite a qauntidade de tapiocas ou salgados: "))
quantacai = int(input("Digite a quantidade de acais: "))
if opcao == "T":
	total = quantopcao*4.5 + quantacai*12
else:
	total = quantopcao*5 + quantacai*12
print(round(total,2))