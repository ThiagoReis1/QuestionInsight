var1 = int(input("Digite a quantidade de horas trabalhadas: "))
Hora = 50.00
x = 1000.00
if var1 <= 20:
	pagamento = var1 * Hora
	print(round(pagamento,2))
else: 
	excedente = var1 - 20
	paga = (excedente * 70) + x 
	print(round(paga,2))

	