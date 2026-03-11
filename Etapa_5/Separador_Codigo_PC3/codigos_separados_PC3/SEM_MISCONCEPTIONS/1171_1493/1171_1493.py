#UNIVERSIDADE FEDERAL DO AMAZONAS
#ENGENHARIA QUIMICA
#MICHAEL EVANGELISTA DA CRUZ - 21600845
#DATA: 05/08/2016
#AVALIACAO PARCIAL 04

n = int(input("N. de termos: "))

contador = 1
x = 1
y = 3
sinal = 1
soma = 0

while(contador <= n):
	soma = ((x**3)/(2+y))*sinal + soma
	
	x = x + 1
	y = y + 2
	sinal = -sinal 
	contador = contador + 1
	
print(round(soma, 8))