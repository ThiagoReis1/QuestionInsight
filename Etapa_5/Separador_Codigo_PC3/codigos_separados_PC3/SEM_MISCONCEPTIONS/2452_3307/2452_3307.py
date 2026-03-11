# Leitura das variaveis
peso = float(input('Entre com um peso: '))
altura = float(input('Entre com uma altura: '))
IMC = peso / altura ** 2

if IMC < 18.5: 
	print('abaixo do peso')
elif 18.5 <= IMC < 25: 
	print('normal')
elif 25 <= IMC < 30:
	print('acima do peso')
else:
	print('obeso')
	
