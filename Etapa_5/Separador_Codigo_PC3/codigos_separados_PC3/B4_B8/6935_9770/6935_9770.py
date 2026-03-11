valor_total = float(input("Digite um valor:"))
codigo = input("opcao de pagamento:").upper()

if codigo == "D":
  	valor_final = valor_total - (valor_total * 0.12)
	
elif codigo == "P":
	valor_final = valor_total - (valor_total * 0.12)
elif codigo == " C":
	vezes = int(input("1 ou 2"))
	if vezes == 1:
		valor_final == valor_total
	else:
		valor_final = valor_total +  (valor_total * 0.07)
print(round(valor_final,2))
	