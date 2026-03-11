from numpy import*

a = input('nomes das atividades fisicas: ').upper()
tempo = array(eval(input('duracao das atividades, respectivamente: ')))

if(a == 'ALONGAMENTO'):
	g1 = 3 * tempo
	print(g1)
elif(a == 'CORRIDA'):
	g2 = 10.3 * tempo
	print(g2)
elif(a == 'DANCA'):
	g3 = 9.7 * tempo
	print(g3)
elif(a == 'ESCALADA'):
	g4 = 9.7 * tempo
	print(g4)
elif(a == 'HIDROGINASTICA'):
	g5 = 5.0 * tempo
	print(g5)
	
cal = sum(tempo)
print