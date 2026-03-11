# faça seu código aqui!
dias = int(input('Digite a quantidade de dias reservados:'))

fixo = 175

if dias < 15:
	total = (dias * fixo) + 20
	print(round(total, 2))
	
elif dias == 15:
	total = (dias * fixo) + 16
	print(round(total, 2))

elif dias > 15:
	total = (dias * fixo) + 10
	print(round(total, 2))
	
	