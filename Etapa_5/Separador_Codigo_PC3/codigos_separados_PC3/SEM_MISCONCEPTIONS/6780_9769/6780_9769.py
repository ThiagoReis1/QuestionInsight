ano = int(input(''))
pais = input('').upper()

idade = 2023 - ano 

if pais == 'B' and idade >= 21:
	print('sim')
	apto = idade - 21
	print(apto)
elif pais == 'B' and idade < 21:
	print('nao')
	fulano = 21 - idade
	print(fulano)
elif pais == 'C' and idade >= 24:
	print('sim')
	apto = idade - 24
	print(apto)
elif pais == 'C' and idade < 24:
	print('nao')
	fulano= 24 - idade
	print(fulano)
else:
	print('invalido')
