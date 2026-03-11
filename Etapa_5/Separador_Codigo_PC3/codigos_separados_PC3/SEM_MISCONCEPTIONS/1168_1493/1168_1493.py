#UNIVERSIDADE FEDERAL DO AMAZONAS
#ENGENHARIA QUIMICA
#MICHAEL EVANGELISTA DA CRUZ - 21600845
#DATA: 05/08/2016
#AVALIACAO PARCIAL 04

n = int(input("No. de termos: "))

contador = 1
x = 1
y = 1
soma = 0
sinal = 1

while(contador <= n):
	soma = -(x**3/(8+y))*sinal + soma
	
	contador = contador + 1
	x = x + 1
	y = y + 2
	sinal = -sinal
	
print(round(soma, 5))