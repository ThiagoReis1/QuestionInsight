an = int(input("Informe o ano de nascimento: "))
p = input('informe o pais: ').upper()
idade = 2023-an

if(p == 'B' and idade >=21):
	print('sim')
	print(idade -21)
elif(p == 'B' and idade < 21):
	print('nao')
	print(21 - idade)
elif(p == 'J' and idade >= 20):
	print('sim')
	print(idade - 20)
elif(p == 'J' and idade < 20):
	print('nao')
	print(20-idade)
else:
	print('invalido')

	