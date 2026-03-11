anoNasc = int(input())
pais = input().upper()
idade = 2023 - anoNasc

if(pais == 'B' or pais == 'R'):
	if(pais == 'B'):
		if(idade >= 21):
			print('sim')
			print(idade - 21)
		else:
			print('nao')
			print(21 - idade)
	elif(pais == 'R'):
		if(idade >= 18):
			print('sim')
			print(idade - 18)
		else:
			print('nao')
			print(18 - idade)
else:
	print('invalido')