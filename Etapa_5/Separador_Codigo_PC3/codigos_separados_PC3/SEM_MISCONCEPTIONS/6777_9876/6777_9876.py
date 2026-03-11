ano = int(input("ano: "))
pais = input("insira ('b') para brasil ou ('i') para inglaterra: ").upper()

idade = 2023 - ano 
if (idade >= 18) and (pais == 'B'):
	print('sim')
	print(idade - 18)
	
elif (idade < 18) and (pais == 'B'):
	print('nao')
	print(18 - idade)

elif (idade >= 17) and (pais == 'I'):
	print('sim')
	print(idade - 17)
elif (idade < 17) and (pais == 'I'):
	print('nao')
	print(17 - idade)
else:
	print('invalido')

