opcao = input("diga sua opcao (T/S):").upper()
quant_g = int(input("qual a quantidade: "))
quant = int(input("quantidade de acais: "))

if opcao == "T":
	valor = 5.50 * quant_g + 10.00 * quant
else:
	valor = 4.00 * quant_g + 10.00 * quant
print(round(valor,2))
	