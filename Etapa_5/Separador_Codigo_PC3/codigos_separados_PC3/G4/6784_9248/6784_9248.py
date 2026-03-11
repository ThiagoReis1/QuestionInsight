nasc = int(input('digite o ano de nascimento:'))
pais = input('digite o pais: (B/R)')
idade = 2023 - nasc

if(pais.upper() == 'B'):
	if(idade >= 21):
		print('sim')
		val = idade - 21
		print(val)
	else:
		print('nao')
		val = 21 - idade
		print(val)
		
elif(pais.upper() == 'R'):
	if(idade >= 18):
		print('sim')
		val = idade - 18
		print(val)
	else:
		print('nao')
		val = 18 - idade
		print(val)
else:
	print('invalido')