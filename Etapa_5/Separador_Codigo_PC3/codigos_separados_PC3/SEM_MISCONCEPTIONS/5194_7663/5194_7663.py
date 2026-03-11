#MISSOES B,A (CHUNIN e JOUNIN)
#Chunin imposto de 15%
#Jounin imposto de 22%

classificacao_missao = input("Qual a classificacao da missao? A/B ")
valor_pago = float(input("Qual o valor pago pela missao? "))

if (classificacao_missao == "B"):
	imposto = valor_pago * 0.15
	valor = valor_pago - imposto
	msg = "Chunin"
	print("Classe:", msg)
	print(round(valor,2))
else:
	imposto = valor_pago * 0.22
	valor = valor_pago - imposto
	msg = "Jounin"
	print("Classe:", msg)
	print(round(valor,2))
	