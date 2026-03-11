from numpy import *

ponto = 10000
n = array(eval(input("")))
cont = 0

while(cont<size(n)):
	if(n[cont] == 1):
		ponto = ponto * 2
	elif(n[cont] == 2):
		ponto = ponto
	elif(n[cont] == 3):
		ponto = ponto/2
	elif(n[cont] == 4):
		ponto = ponto/4
	cont += 1
print(round(ponto,2))
