opcao = input("DIGITE 'B' se for bolo ou 'C' se for croissant: ").upper()
q1 = int(input("Digite a quantidade de fatias de bolo ou croissant: "))
q2 = int(input("Digite aa quantidade de cappuccinos: "))

if (opcao == 'B'):
	total = (3 * q1) + (5.5 * q2)
	print(total)
	
else:
	total = (6 * q1) + (5.5 * q2)
	print(total)