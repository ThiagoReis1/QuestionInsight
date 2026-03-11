unidade = input()
valor = float(input())

if(unidade.lower() == 'm'):
	resultado = valor/2.35215

if(unidade.lower() == 'k'):
	resultado = 2.35215 * valor
	
print(round(resultado, 2))