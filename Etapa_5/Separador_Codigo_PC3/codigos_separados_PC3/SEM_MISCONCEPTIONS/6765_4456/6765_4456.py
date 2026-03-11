ano = int(input())
pais = input()
idade = 2023 - ano

if (pais.upper() == 'B' and idade >= 18):
	print('sim')
	print(idade - 18)
elif pais.upper() == 'R' and idade >= 21:
	print('sim')
	print(idade - 21)
elif pais.upper() == 'B' and idade < 18:
	print('nao')
	print(18 - idade)
elif pais.upper() == 'R' and idade < 21:
	print('nao')
	print(21-idade)
else:
	print('invalido')
