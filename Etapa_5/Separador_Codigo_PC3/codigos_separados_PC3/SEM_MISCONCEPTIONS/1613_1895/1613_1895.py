from numpy import *

atividade = array(eval(input("digite as atividades")))
tempo = array(eval(input("digite os tempo")))

i = size(atividade)
cont = 0
cal = 0
while(cont < i):
	if( atividade[cont] == 'ALONGAMENTO' ):
		cal = cal + 3.0*tempo[cont]
	if( atividade[cont] == 'CORRIDA' ):
		cal = cal + 10.3*tempo[cont]
	if( atividade[cont] == 'DANCA' ):
		cal = cal + 6.7*tempo[cont]
	if( atividade[cont] == 'ESCALADA' ):
		cal = cal + 9.7*tempo[cont]
	if( atividade[cont] == 'HIDROGINASTICA' ):
		cal = cal + 5.0*tempo[cont]
	cont = cont + 1
	
print(round(cal,2))