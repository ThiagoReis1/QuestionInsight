from numpy import *

ss = input("Digite 'D' para doces, 'S' para salgados e 'I' para integrais: ").upper()

doces = 2.25
salgados = 4.0
integrais = 6.90

i = 0 # indice
qd = 0 # quantidade de doce
qs = 0 # quantidade de salgado
qi = 0 # quantidade de integrais
total = 0 # variavel acumuladora do total de compras

while (i < len(ss)):
	p = ss[i]
	
	if (p == 'D'):
		qd = qd +1
		
	elif (p == 'S'):
		qs = qs + 1
		
	elif (p == 'I'):
		qi = qi + 1
		
	i = i + 1
	
total = (qd * doces) + (qs * salgados) + (qi * integrais)

print(round(total, 2))