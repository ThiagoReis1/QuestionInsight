opcao = input("L ou P: ")
qtd = int(input("Quantidade: "))
qtd_rf = int(input("Refrigerantes: "))

if opcao.upper() == "L":
	total = qtd * 6.00 + qtd_rf * 3.00
else:
	total = qtd * 13.50 + qtd_rf * 3.00
print(round(total,2))