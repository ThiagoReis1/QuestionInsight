escolha = input("insira o item escolhido (T/S): ").upper()
quant = int(input("insira a quantidade do item escolhido: "))
quant_acai = int(input("insira a quantidade de acais: "))

tapioca = 5.5
salgado = 4.0
acai = 10.0

if escolha == "T":
	preco = quant * tapioca + acai * quant_acai
else:
	preco = quant * salgado + acai * quant_acai
	
print(preco)